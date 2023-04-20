function solution(array) {
    const frequencyMap = array.reduce((acc, cur) => {
        acc.set(cur, (acc.get(cur) || 0) + 1)
        return acc
    }, new Map())
    
    const mode = Math.max(...frequencyMap.values())
    
    const NumberOfMode = [...frequencyMap.values()].filter((fre) => fre === mode)
    
    if(NumberOfMode.length > 1) return -1
    
    for(let [key, value] of frequencyMap) {
        if(value === mode) return key
    }
}