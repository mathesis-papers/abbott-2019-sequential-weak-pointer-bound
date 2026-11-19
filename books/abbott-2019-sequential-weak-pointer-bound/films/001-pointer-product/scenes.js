'use strict';

const center = W / 2;
FILM.hud = false;
const label = (s, x, y, size, a = 1, c = C.white, fam = F.math) =>
  txt(s, x, y, { size, a, c, fam, w: 700, align: 'center' });

function heading(zh, en) {
  label(zh, center, 150, 66, 1, C.white, F.zh);
  label(en, center, 215, 35, 1, C.cyan, F.disp);
}

function pointerScale(x, y, index, displacement, a) {
  label('x' + index, x, y - 105, 43, a);
  line(x - 172, y, x + 172, y, C.white, a * 0.65, 3);
  for (const tick of [-144, -96, -48, 0, 48, 96, 144]) {
    const h = tick === 0 ? 16 : 8;
    line(x + tick, y - h, x + tick, y + h, C.white, a * 0.75, 2);
  }
  label('0', x, y + 55, 31, a);
  const needle = x + displacement;
  arrow(needle, y - 76, needle, y - 5, C.now, a, 5);
}

SCENES.readings = S => {
  heading('三个读数相乘', 'Multiply the three readings');
  const move = at(S, 0, 3);
  pointerScale(465, 473, '₁', 97 * move, 1);
  pointerScale(960, 473, '₂', -119 * move, 1);
  pointerScale(1455, 473, '₃', 71 * move, 1);
  label('E[x₁x₂x₃] / (h₁h₂h₃)', center, 667, 56, at(S, 1, 0.7));
  label('μₙ ≥ −1/8 ?', center, 795, 65, at(S, 2, 0.8), C.now);
};

function projectionAxes(x, y, route, progress) {
  const unit = 248;
  arrow(x - 80, y, x + unit + 170, y, C.white, 0.55, 2);
  arrow(x, y + 39, x, y - unit - 52, C.white, 0.55, 2);
  line(x, y, x + unit + 25, y - unit - 25, C.cyan, 0.48, 2.5);
  label('y = x', x + unit + 72, y - unit, 25, 0.8, C.cyan);
  label('(0,1)', x - 72, y - unit + 8, 27);
  ring(x, y - unit, 6, C.white, 1, 5);
  let px = x;
  let py = y - unit;
  for (let i = 0; i < route.length; i++) {
    const [dx, dy] = route[i];
    const a = clamp(progress * route.length - i);
    const nx = x + unit * dx;
    const ny = y - unit * dy;
    arrow(px, py, lerp(px, nx, a), lerp(py, ny, a), C.now, a, 4);
    ring(nx, ny, 6, C.now, a, 5);
    px = nx;
    py = ny;
  }
}

SCENES.orders = S => {
  heading('投影的次序', 'The order of projections');
  label('Q → P', 525, 302, 41, at(S, 1, 0.5));
  label('P → Q', 1305, 302, 41, at(S, 2, 0.5));
  const first = at(S, 1, 4);
  const second = at(S, 2, 2);
  projectionAxes(390, 650, [[0.5, 0.5], [0.5, 0]], first);
  projectionAxes(1190, 650, [[0, 0]], second);
  label('(1/2,0)', 570, 710, 34, first, C.now);
  label('(0,0)', 1190, 710, 34, second, C.now);
  label('Jₚ(X) = (PX + XP)/2', center, 811, 47, at(S, 3, 0.75));
};

SCENES.witness = S => {
  heading('三维反例', 'The three-dimensional witness');
  label('e₃ = (0, 0, 1)', center, 316, 50, at(S, 0, 0.55));
  const planes = at(S, 1, 0.8);
  label('P₂P₃e₃ = (1/2, 1/4, 1/4)', 535, 428, 42, planes);
  label('P₃P₂e₃ = (1/4, 1/2, 1/4)', 1385, 428, 42, planes);
  label('B e₃ = (3/4, 3/4, 1/2)', center, 525, 48, planes, C.cyan);
  label('P₁e₃ = (−1, −1, 1)/3', center, 626, 48, at(S, 2, 0.65));
  const result = at(S, 3, 0.8);
  label('½ (−1/4 − 1/4 + 1/6) = −1/6 < −1/8', center, 779, 58, result, C.now);
};

function lowerQuadratic(c, a) {
  const left = 1040;
  const width = 640;
  const zero = 474;
  const scale = 900;
  const midpoint = (1 - c) / 2;
  const halfWidth = (1 + c) / 2;
  const vertex = halfWidth / (2 * midpoint);
  const f = s => midpoint * s * s - halfWidth * s;
  arrow(left - 48, zero, left + width + 76, zero, C.white, 0.55, 2);
  arrow(left, zero + 298, left, zero - 113, C.white, 0.55, 2);
  label('0', left - 14, zero - 22, 26);
  label('1', left + width, zero - 22, 26);
  label('s', left + width + 65, zero - 26, 30);
  for (let i = 0; i < 64; i++) {
    const s = i / 64;
    const next = (i + 1) / 64;
    line(left + width * s, zero - scale * f(s),
      left + width * next, zero - scale * f(next), C.cyan, a, 4);
  }
  const vx = left + width * vertex;
  const vy = zero - scale * f(vertex);
  dashed(vx, zero, vx, vy, C.now, a, 2);
  ring(vx, vy, 9, C.now, a, 7);
  label('−F(c)', vx, vy + 64, 38, a, C.now);
}

SCENES.quadratic = S => {
  heading('下一步的下界', 'The floor after one more projection');
  const c = lerp(0, 0.24, ease(at(S, 3, 5)));
  label('[−c, 1]', 535, 390, 76, at(S, 0, 0.5));
  label('c = ' + c.toFixed(2), 535, 442, 30, at(S, 2, 0.75));
  label('s = ‖Pψ‖', 535, 493, 54, at(S, 1, 0.65));
  const curve = at(S, 2, 0.75);
  label('as² − bs', 535, 618, 74, curve, C.cyan);
  label('a = (1−c)/2,   b = (1+c)/2', 535, 704, 35, curve);
  lowerQuadratic(c, curve);
};

function recurrence(c) {
  return (1 + c) ** 2 / (8 * (1 - c));
}

SCENES.lengths = S => {
  heading('有限长度的下界', 'The floor at each finite length');
  const x = n => 340 + (n - 1) * 90;
  const y = c => 315 + 1120 * c;
  arrow(285, y(0), 1760, y(0), C.white, 0.6, 2);
  label('n', 1780, y(0) + 15, 30);
  label('−cₙ', 225, y(0) + 12, 30);
  const limit = at(S, 2, 0.85);
  dashed(285, y(1 / 3), 1680, y(1 / 3), C.now, limit, 3);
  label('−1/3', 260, y(1 / 3) + 11, 36, limit, C.now);
  let c = 0;
  for (let n = 1; n <= 15; n++) {
    const a = n <= 2 ? at(S, 0, 0.8) : n === 3 ? at(S, 1, 0.8) : at(S, 2, 0.65, (n - 4) * 0.16);
    ring(x(n), y(c), n <= 3 ? 8 : 5, C.cyan, a, 5);
    if (n <= 3 || n === 15) label(String(n), x(n), y(0) - 22, 31, a);
    c = recurrence(c);
  }
  label('0', 330, y(0) + 61, 34, at(S, 0, 0.8));
  label('−1/8', x(2), y(1 / 8) + 50, 35, at(S, 0, 0.8));
  label('−81/448', x(3), y(81 / 448) + 75, 35, at(S, 1, 0.8));
  label('Haobo Ma · Wenlin Zhang', center, 786, 35, at(S, 3, 0.75));
};

FILM.poster = () => {
  const t = TL.scenes[2].start + 1;
  background(t, TL.scenes[2], 2, 4);
  grid(t, 0.4);
  label(DATA.film.title_zh, center, 262, 79, 1, C.white, F.zh);
  label(DATA.film.title, center, 375, 63, 1, C.cyan, F.disp);
  const left = 460;
  const right = 1480;
  const x = value => lerp(left, right, (value + 0.22) / 0.24);
  arrow(left, 604, right, 604, C.white, 0.72, 3);
  for (const [value, caption, color] of [
    [-1 / 6, '−1/6', C.now],
    [-1 / 8, '−1/8', C.cyan],
    [0, '0', C.white],
  ]) {
    line(x(value), 570, x(value), 635, color, 1, 5);
    ring(x(value), 604, 6, color, 1, 5);
    label(caption, x(value), 704, 62, 1, color);
  }
  label('Haobo Ma · Wenlin Zhang', center, 932, 37, 1, C.white, F.disp);
};
