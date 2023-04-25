function solution(numbers) {
    return Array.from({length : 10}, (_, idx) => idx)
                .filter((num, idx) => !numbers.includes(num))
                .reduce((acc, cur) => acc + cur, 0)
}