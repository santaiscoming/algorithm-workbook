function solution(n, t) {
    const wasteTime = Array.from({length : t}, () => n)
    return wasteTime.reduce((acc, cur) => acc * 2 ,n)
}