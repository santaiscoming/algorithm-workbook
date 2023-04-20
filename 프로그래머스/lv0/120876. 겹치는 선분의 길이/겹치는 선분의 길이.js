function solution(lines) {
  let result = 0;
  // 범위가 -100 < < 100
  const lineDots = Array.from({ length: 200 }, () => 0);

  // left 부터 1씩 증가하면서 1 더해줌
  // 만약 겹치는 공간이 있으면 1 또 더해져서 2가 될것
  lines.forEach(([left, right]) => {
    for (let j = left; j < right; j++) {
      lineDots[j + 100] += 1;
    }
  });

  lineDots.forEach((dot, idx) => {
    if (lineDots[idx] > 1) result += 1;
  });

  return result;
}
