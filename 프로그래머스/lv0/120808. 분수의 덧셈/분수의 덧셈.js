function solution(numer1, denom1, numer2, denom2) {
    // 손코딩의 위대함
  let denom = numer1 * denom2 + numer2 * denom1;
  let numer = denom1 * denom2;
  let sameMax = 1;

    // 최대공약수
  for (let i = 1; i <= denom; i++) {
    if (denom % i === 0 && numer % i === 0) {
      sameMax = i;
    }
  }
  return [denom / sameMax, numer / sameMax];
}
