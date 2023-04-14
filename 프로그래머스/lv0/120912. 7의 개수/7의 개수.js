function solution(array) {
    return [...array.join('')].filter((num) => Number(num) === 7).length
}