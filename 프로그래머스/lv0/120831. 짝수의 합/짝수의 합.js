function solution(n) {
  const arr = Array.from({ length: n }, (_, i) => i + 1);
  const sum = arr.reduce((acc, cur) => cur % 2 === 0 ? acc + cur : acc, 0); // 짝수만 더하여 합계 계산
  return sum;
}