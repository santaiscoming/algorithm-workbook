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
    
    // 앞에서 탐색한 indexOf와 뒤에서 탐색한 lastIndexOf의 값이 같다면 중복 X
    //    let res = [];
    // for (let c of s) if (s.indexOf(c) === s.lastIndexOf(c)) res.push(c);
    // return res.sort().join('');
}