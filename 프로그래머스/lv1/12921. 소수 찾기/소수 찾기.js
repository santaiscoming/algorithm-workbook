function solution(n) {
    let count = 0;
    
    if (n === 1) return 0;
    
    for (let i = 2; i < n; i++) {
      if (n % i === 0) continue;
        count += 1;
    }

    return count
}