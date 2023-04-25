// 최대공약수를 구하는 함수
function getGCD(a, b) {
  if (b === 0) {
    return a;
  }
  return getGCD(b, a % b);
}

// 최대공배수를 구하는 함수
function getLCM(a, b) {
  return (a * b) / getGCD(a, b);
}


function solution(n, m) {
    
    return [getGCD(n, m), getLCM(n, m)]
}