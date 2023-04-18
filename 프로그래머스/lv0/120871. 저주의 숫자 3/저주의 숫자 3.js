function solution(n) {
    const arr = Array.from({length : n * 3}, (_, idx) => idx + 1);
    
    const strangeLanguage = arr.filter((num) => num % 3 !== 0 && !String(num).includes('3'))
    
    return strangeLanguage[n - 1]
}