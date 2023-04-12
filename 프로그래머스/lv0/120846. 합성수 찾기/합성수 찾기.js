const mineralWaterCount = (num) => {
    const arr = Array.from({length : num}, (_, idx) => idx + 1)
    const arr2 = arr.map((num) => {
        const mineralWater = []
        for(let i = 1; i <= num; i++) {
            if(num % i === 0) mineralWater.push(i)
        }
        return mineralWater
    })
    return arr2
}


function solution(n) {
    let count = 0;
    
    const mineralWaterMap = new Map()
    
    const mineralWater = mineralWaterCount(n)
    
    mineralWater.forEach((arr, idx) => {
        mineralWaterMap.set(idx + 1, arr.length)
    })
    
    const countArr = [...mineralWaterMap.values()];
    
    countArr.forEach((val) => {
        if(val >= 3) count += 1;
    })
    
    return count
}