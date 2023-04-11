function solution(n, numlist) {
    return numlist.filter((num) => Number.isInteger(num / n))
}