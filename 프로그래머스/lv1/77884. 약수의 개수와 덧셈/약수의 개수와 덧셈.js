const getWater = (num) => {
    return Array.from({length : num}, (_, idx) => idx + 1)
                .filter((e) => num % e === 0)
}

function solution(left, right) {
    return Array.from({length : right - left + 1}, (_, idx) => idx + left)
                .map((num) => {
                     if(getWater(num).length % 2 === 0) return Math.max(...getWater(num))
                     return -Math.max(...getWater(num))
                    })
                .reduce((acc, cur) => acc + cur, 0)
}