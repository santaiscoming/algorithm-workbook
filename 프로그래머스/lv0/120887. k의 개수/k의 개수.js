function solution(i, j, k) {
    const nums = Array.from({length : j - i  + 1}, (_, idx) => idx + i)
    
    const allNums  = nums.map((num) => [...String(num)]).flat();
    
    return allNums.filter((num) => Number(num) === k).length
}