function solution(s1, s2) {
    return s1.filter((str) => s2.includes(str)).length
}