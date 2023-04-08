function solution(slice, n) {
    if (n % slice === 0) return n / slice
    return Math.floor(n / slice) + 1
}