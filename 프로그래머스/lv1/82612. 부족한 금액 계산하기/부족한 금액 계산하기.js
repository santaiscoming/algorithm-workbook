function solution(price, money, count) {
    const result = Array.from({length : count}, (_, idx) => idx + 1)
                        .map((idx) =>  idx * price)
                        .reduce((acc, cur) => acc - cur, money)

    if(result >= 0) return 0
    return Math.abs(result)
}