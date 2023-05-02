function solution(n) {
  const primes = [2];
  
  for (let i = 3; i <= n; i++) {
    let isPrime = true;
    const sqrtI = Math.sqrt(i);
    for (let j = 0; primes[j] <= sqrtI; j++) {
      if (i % primes[j] === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) primes.push(i);
  }
  
  return primes.length;
}
