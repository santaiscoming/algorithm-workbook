const isPrime = (num) => {
    if(num === 1) return false
    for(let i = 2; i <= Math.sqrt(num); i++) {
        if(num % i === 0) return false;
    }
    return true;
}

function solution(nums) {
    const dfs = (depth, start, sum) => {
    if (depth === 3) {
      if (isPrime(sum)) return 1;
      return 0;
    }

    let count = 0;

    for (let i = start; i < nums.length; i++) {
      count += dfs(depth + 1, i + 1, sum + nums[i]);
    }

    return count;
  };

  return dfs(0, 0, 0);
}