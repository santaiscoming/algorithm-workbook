function solution(n) {
    const arr = Array.from({length : n}, (_, idx) => idx + 1)
    return arr.filter((num) => arr.length % num === 0)
}