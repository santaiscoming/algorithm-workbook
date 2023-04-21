function solution(num) {
    const result = ['Odd', 'Even']
    return num % 2 === 0 ? result[1] : result[0]
}