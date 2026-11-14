"""Exact identities and finite matrix checks for note.tex."""

import json
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as symbolic


def exact_zero(matrix):
    return all(symbolic.simplify(entry) == 0 for entry in matrix)


def jordan(projection, operator):
    return (projection @ operator + operator @ projection) / 2


def check_symbolic_identities():
    constant = symbolic.symbols('constant', real=True, nonnegative=True)
    center = (1 - constant) / 2
    radius = (1 + constant) / 2
    overlap = (1 + constant) / (2 * (1 - constant))
    next_bound = (1 + constant) ** 2 / (8 * (1 - constant))
    lower = symbolic.sqrt((1 - overlap) / 2)
    upper = symbolic.sqrt((1 + overlap) / 2)
    state = symbolic.Matrix([lower, upper])
    direction = symbolic.Matrix([-lower, upper])
    projection = direction * direction.T
    operator = symbolic.diag(1, -constant)
    transformed = (projection * operator + operator * projection) / 2
    assert exact_zero(transformed * state + next_bound * state)
    assert symbolic.simplify((state.T * state)[0] - 1) == 0
    assert symbolic.simplify((direction.T * direction)[0] - 1) == 0
    assert symbolic.simplify((direction.T * state)[0] - overlap) == 0
    assert symbolic.factor(next_bound - constant - (1 - 3 * constant) ** 2 / (8 * (1 - constant))) == 0
    assert symbolic.factor(symbolic.Rational(1, 3) - next_bound - (1 - 3 * constant) * (constant + 5) / (24 * (1 - constant))) == 0
    assert symbolic.factor(center * overlap**2 - radius * overlap + next_bound) == 0
    delta = symbolic.symbols('delta', positive=True)
    delta_next = symbolic.factor(symbolic.Rational(1, 3) - next_bound.subs(constant, symbolic.Rational(1, 3) - delta))
    assert symbolic.factor(delta_next - delta * (16 - 3 * delta) / (16 + 24 * delta)) == 0
    assert symbolic.factor(1 / delta_next - 1 / delta - 27 / (16 - 3 * delta)) == 0
    return ['one-step minimum and eigenvector', 'unit norms and overlap',
            'recurrence increment and invariant interval', 'delta recurrence and reciprocal increment']


def rational_witness():
    half = symbolic.Rational(1, 2)
    projections = [
        symbolic.Matrix([[1, 1, -1], [1, 1, -1], [-1, -1, 1]]) / 3,
        symbolic.Matrix([[1, 0, 0], [0, half, half], [0, half, half]]),
        symbolic.Matrix([[half, 0, half], [0, 1, 0], [half, 0, half]]),
    ]
    for projection in projections:
        assert projection == projection.T and projection * projection == projection
    assert [projection.rank() for projection in projections] == [1, 2, 2]
    operator = projections[-1]
    for projection in reversed(projections[:-1]):
        operator = (projection * operator + operator * projection) / 2
    state = symbolic.Matrix([0, 0, 1])
    assert (state.T * state)[0] == 1
    assert (state.T * operator * state)[0] == -symbolic.Rational(1, 6)
    assert operator[2, 2] < -symbolic.Rational(1, 8)
    for ordering in [(2, 1, 0), (1, 2, 0)]:
        ordered = symbolic.eye(3)
        for index in ordering:
            ordered = ordered * projections[index]
        assert (state.T * ordered * state)[0] == -symbolic.Rational(1, 6)
    return projections


def exact_extremizer():
    identity = symbolic.eye(3)
    state = identity[:, 0]
    operator = identity - state * state.T
    bound = Fraction(0)
    for step in range(1, 3):
        overlap = symbolic.Rational(1 + bound) / (2 * symbolic.Rational(1 - bound))
        lower = symbolic.sqrt((1 - overlap) / 2)
        upper = symbolic.sqrt((1 + overlap) / 2)
        normal = upper * identity[:, step] + lower * state
        projection = identity - normal * normal.T
        assert exact_zero(projection * projection - projection)
        assert projection == projection.T and symbolic.trace(projection) == 2
        operator = ((projection * operator + operator * projection) / 2).applyfunc(symbolic.simplify)
        state = (lower * identity[:, step] + upper * state).applyfunc(symbolic.simplify)
        bound = (1 + bound) ** 2 / (8 * (1 - bound))
        assert exact_zero(operator * state + symbolic.Rational(bound) * state)
    assert bound == Fraction(81, 448)
    assert symbolic.simplify((state.T * operator * state)[0]) == -symbolic.Rational(81, 448)


def gaussian_checks(projections):
    position, left, right, centered = symbolic.symbols('position left right centered', real=True)
    sigma, coupling = symbolic.symbols('sigma coupling', positive=True)
    midpoint = (left + right) / 2
    assert symbolic.expand((position - left)**2 + (position - right)**2 - 2 * (position - midpoint)**2 - (left - right)**2 / 2) == 0
    gaussian = symbolic.exp(-centered**2 / (2 * sigma**2)) / symbolic.sqrt(2 * symbolic.pi * sigma**2)
    mass = symbolic.integrate(gaussian, (centered, -symbolic.oo, symbolic.oo))
    moment = symbolic.integrate(centered * gaussian, (centered, -symbolic.oo, symbolic.oo))
    assert mass == 1 and moment == 0
    first_moment = (midpoint * mass + moment) * symbolic.exp(-(left - right)**2 / (8 * sigma**2))
    for left_bit in [0, 1]:
        for right_bit in [0, 1]:
            expected = coupling * symbolic.Rational(left_bit + right_bit, 2) * symbolic.exp(-coupling**2 * (left_bit - right_bit)**2 / (8 * sigma**2))
            assert symbolic.simplify(first_moment.subs({left: left_bit * coupling, right: right_bit * coupling}) - expected) == 0
            assert symbolic.limit(expected / coupling, coupling, 0, dir='+') == symbolic.Rational(left_bit + right_bit, 2)
    numeric = [np.array(projection, dtype=float) for projection in projections]
    controls = []
    for epsilon in [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]:
        operator = np.diag([0.0, 0.0, 1.0])
        for projection, width, strength in zip(numeric, [1.0, 1.5, 2.0], [1.0, 2.0, 3.0]):
            complement = np.eye(3) - projection
            overlap = np.exp(-(epsilon * strength)**2 / (8 * width**2))
            operator = projection @ operator @ projection + overlap * (projection @ operator @ complement + complement @ operator @ projection) / 2
        normalized = float(np.trace(operator))
        error = abs(normalized + 1 / 6)
        assert error < epsilon**2
        controls.append({'epsilon': epsilon, 'normalized_pointer_product': normalized, 'absolute_error': error})
    return controls


def construction_checks():
    controls = []
    for length in [1, 2, 3, 4, 8, 16, 32, 64]:
        identity = np.eye(length)
        state = identity[:, 0]
        operator = identity - np.outer(state, state)
        projections = [operator.copy()]
        bound = 0.0
        maximum_residual = 0.0
        for step in range(1, length):
            overlap = (1 + bound) / (2 * (1 - bound))
            lower, upper = np.sqrt((1 - overlap) / 2), np.sqrt((1 + overlap) / 2)
            normal = upper * identity[:, step] + lower * state
            projection = identity - np.outer(normal, normal)
            assert np.linalg.norm(projection @ projection - projection) < 1e-11
            assert abs(np.trace(projection) - (length - 1)) < 1e-11
            operator = jordan(projection, operator)
            state = lower * identity[:, step] + upper * state
            bound = (1 + bound)**2 / (8 * (1 - bound))
            residual = float(np.linalg.norm(operator @ state + bound * state))
            maximum_residual = max(maximum_residual, residual)
            assert residual < 1e-11
            assert np.linalg.norm(operator[:, step + 1:] - identity[:, step + 1:]) < 1e-11
            projections.append(projection)
        nested = projections[0]
        for projection in projections[1:]:
            nested = jordan(projection, nested)
        assert np.linalg.norm(nested - operator) < 1e-11
        eigenvalues = np.linalg.eigvalsh(nested)
        assert abs(eigenvalues[0] + bound) < 1e-11
        assert eigenvalues[-1] <= 1 + 1e-11
        assert abs(state @ nested @ state + bound) < 1e-11
        assert abs(state @ state - 1) < 1e-11
        controls.append({'n': length, 'dimension': length, 'projection_rank': length - 1,
                         'minimum_eigenvalue': float(eigenvalues[0]), 'predicted_minimum': -bound,
                         'maximum_eigenvector_residual': maximum_residual})
    return controls


def random_checks():
    generator = np.random.default_rng(20261005)
    count = 0
    for dimension in [2, 3, 4, 6, 8]:
        for length in [1, 2, 3, 5, 12, 30]:
            for sample in range(12):
                operator = np.eye(dimension, dtype=complex)
                for step in range(length):
                    basis, triangular = np.linalg.qr(generator.normal(size=(dimension, dimension)) + 1j * generator.normal(size=(dimension, dimension)))
                    rank = int(generator.integers(1, dimension))
                    projection = basis[:, :rank] @ basis[:, :rank].conj().T
                    operator = jordan(projection, operator)
                eigenvalues = np.linalg.eigvalsh(operator)
                assert eigenvalues[0] >= -1 / 3 - 1e-11
                assert eigenvalues[-1] <= 1 + 1e-11
                count += 1
    return count


def sibling_checks(projections):
    parameter = symbolic.symbols('overlap', real=True)
    symbolic_operator = symbolic.Matrix(3, 3, lambda row, column: symbolic.symbols(f'entry_{row}_{column}'))
    for projection in projections:
        complement = symbolic.eye(3) - projection
        direct = projection * symbolic_operator * projection + parameter * (
            projection * symbolic_operator * complement + complement * symbolic_operator * projection) / 2
        convex = parameter * (projection * symbolic_operator + symbolic_operator * projection) / 2 + (
            1 - parameter) * projection * symbolic_operator * projection
        assert exact_zero(direct - convex)
        assert exact_zero(parameter * projection + (1 - parameter) * projection * projection - projection)
    generator = np.random.default_rng(20261113)
    counts = {'finite_gaussian_envelopes': 0, 'positive_contractions': 0,
              'commuting_projection_products': 0, 'hermitian_norm_bounds': 0}
    maximum_discrepancy = 0.0
    for dimension in [2, 3, 5, 8]:
        for length in [1, 2, 3, 5, 12, 20]:
            bound = 0.0
            for step in range(1, length):
                bound = (1 + bound) ** 2 / (8 * (1 - bound))
            for sample in range(6):
                gaussian_operator = np.eye(dimension, dtype=complex)
                effect_operator = np.eye(dimension, dtype=complex)
                hermitian_operator = np.eye(dimension, dtype=complex)
                commuting_operator = np.eye(dimension)
                commuting_product = np.eye(dimension)
                norm_product = 1.0
                for step in range(length):
                    basis, triangular = np.linalg.qr(generator.normal(size=(dimension, dimension)) + 1j * generator.normal(size=(dimension, dimension)))
                    rank = int(generator.integers(0, dimension + 1))
                    projection = basis[:, :rank] @ basis[:, :rank].conj().T
                    overlap = float(generator.choice([0.0, 0.1, 0.5, 0.9, 1.0]))
                    gaussian_operator = overlap * jordan(projection, gaussian_operator) + (1 - overlap) * projection @ gaussian_operator @ projection
                    effect = (basis * generator.uniform(0, 1, dimension)) @ basis.conj().T
                    effect_operator = jordan(effect, effect_operator)
                    observable = (basis * generator.uniform(-2, 2, dimension)) @ basis.conj().T
                    hermitian_operator = jordan(observable, hermitian_operator)
                    norm_product *= np.linalg.norm(observable, 2)
                    diagonal_projection = np.diag(generator.integers(0, 2, dimension))
                    commuting_product = diagonal_projection @ commuting_product
                    commuting_operator = overlap * jordan(diagonal_projection, commuting_operator) + (1 - overlap) * diagonal_projection @ commuting_operator @ diagonal_projection
                for operator in [gaussian_operator, effect_operator]:
                    eigenvalues = np.linalg.eigvalsh(operator)
                    assert eigenvalues[0] >= -bound - 1e-11
                    assert eigenvalues[-1] <= 1 + 1e-11
                discrepancy = float(np.linalg.norm(commuting_operator - commuting_product))
                maximum_discrepancy = max(maximum_discrepancy, discrepancy)
                assert discrepancy < 1e-11
                assert np.linalg.norm(hermitian_operator, 2) <= norm_product + 1e-11
                for key in counts:
                    counts[key] += 1
    return {'symbolic_gaussian_map_decomposition': True,
            'symbolic_final_pointer_independence': True,
            'finite_controls': counts,
            'commuting_maximum_discrepancy': maximum_discrepancy,
            'seed': 20261113}


def main():
    symbolic_checks = check_symbolic_identities()
    projections = rational_witness()
    exact_extremizer()
    prefix = []
    bound = Fraction(0)
    for length in range(1, 9):
        prefix.append({'n': length, 'minimum': str(-bound)})
        assert 0 <= bound < Fraction(1, 3)
        bound = (1 + bound)**2 / (8 * (1 - bound))
    assert prefix[1]['minimum'] == '-1/8'
    assert prefix[2]['minimum'] == '-81/448'
    assert prefix[3]['minimum'] == '-279841/1315328'
    result = {
        'status': 'pass',
        'scope': 'Exact algebra and finite matrix checks supporting the written proofs in note.tex.',
        'software': {'python': platform.python_version(), 'numpy': np.__version__, 'sympy': symbolic.__version__},
        'symbolic_checks': symbolic_checks,
        'rational_counterexample': {'dimension': 3, 'ranks': [1, 2, 2], 'mean': '-1/6'},
        'exact_extremizer': {'dimension': 3, 'ranks': [2, 2, 2], 'mean': '-81/448'},
        'minimum_prefix': prefix,
        'gaussian_controls': gaussian_checks(projections),
        'attainment_controls': construction_checks(),
        'random_control_count': random_checks(),
        'random_seed': 20261005,
        'sibling_checks': sibling_checks(projections),
        'numeric_absolute_tolerance': 1e-11,
    }
    output = Path(__file__).with_name('verification.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS: exact witnesses, symbolic identities, Gaussian moments, eight attaining constructions, 360 matrix controls and four sets of 144 sibling controls.')


if __name__ == '__main__':
    main()
