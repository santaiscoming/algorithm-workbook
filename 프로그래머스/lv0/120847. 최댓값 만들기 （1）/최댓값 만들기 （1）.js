function solution(numbers) {
    let max = Number.MIN_SAFE_INTEGER
    for(let i = 0; i < numbers.length; i++) {
        for(let j = i + 1; j < numbers.length; j++) {
            const multiplication = numbers[i] * numbers[j]
            multiplication > max ? max = multiplication : max
        }
    }
    return max
}