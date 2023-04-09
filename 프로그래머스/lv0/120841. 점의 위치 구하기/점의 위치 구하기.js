function solution(dot) {
  const [x, y] = dot;
  let quadrant;

  switch (Math.sign(x)) {
    case 1:
      quadrant = Math.sign(y) > 0 ? 1 : 4;
      break;
    case -1:
      quadrant = Math.sign(y) > 0 ? 2 : 3;
  }

  return quadrant;
}
