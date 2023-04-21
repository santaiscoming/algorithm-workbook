function solution(n) {
    const arr = Array.from({length : n}, (_, idx) => idx + 1)
                     .filter((num) => n % num === 1 && num < n)

    return arr[0] < n ? arr[0] : n
}