function solution(dots) {
  let answer = 0;

  const getInclination = (a, b) => (b[1] - a[1]) / (b[0] - a[0]);

  const isEqual = (a, b, c, d) => getInclination(a, b) === getInclination(c, d);

  if (isEqual(dots[0], dots[1], dots[2], dots[3]) ||
      isEqual(dots[0], dots[2], dots[1], dots[3]) ||
      isEqual(dots[0], dots[3], dots[1], dots[2])) {
    answer = 1;
  }

  return answer;
}
