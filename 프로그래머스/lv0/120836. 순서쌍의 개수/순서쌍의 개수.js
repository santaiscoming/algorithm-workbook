function solution(n) {
  //약수 구하기
    return Array.from({length : n}, (_, idx) => idx + 1).filter((num) => n % num === 0).length
}
