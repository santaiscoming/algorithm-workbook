function solution(n) {
  const arr = [];
  for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= n; j++) {
      if (i * j > n) break;
      if (i * j === n) arr.push([i, j]);
    }
  }
    return arr.length
}
