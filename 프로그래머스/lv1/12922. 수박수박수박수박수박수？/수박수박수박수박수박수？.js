function solution(n) {
    return Array.from({length : n}, (_, idx) => idx + 1)
                .map((num) => num % 2 === 0 ? '박' : '수')
                .join('')
}