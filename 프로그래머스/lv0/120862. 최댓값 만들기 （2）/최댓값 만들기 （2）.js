function solution(numbers) {
    numbers.sort((a, b) => b - a)
    const headMax = numbers[0] * numbers[1]
    const tailMax = numbers[numbers.length - 1] * numbers[numbers.length - 2]
    return Math.max(headMax, tailMax)
}