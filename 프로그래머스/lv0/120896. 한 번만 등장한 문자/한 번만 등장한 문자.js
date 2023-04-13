function solution(s) {
    let result = [];
    const strFrequency = new Map()
    
    // 출현 빈도를 구해주자
    const frequencyMap = [...s].reduce((acc, cur) => strFrequency.set(cur, (strFrequency.get(cur) || 0) + 1), new Map())
    
    // 출현 빈도가 value로 저장되었으니 value값이 1인것만 반환하자
    const sArr = [...s]
    sArr.forEach((str) => {
        if(frequencyMap.get(str) === 1) result.push(str)
    })
    return result.sort().join('')
}