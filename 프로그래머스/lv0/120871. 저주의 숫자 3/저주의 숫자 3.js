function solution(n) {
    // n까지 증가시키면서 list.push(num)
        // if : currnetNum % 3 === 0 && String(currentNum).include(3) -> currentNum++, continue
    let count = n
    const villageNumList = [];
    let currentNum = 1
    while(true) {
        if(villageNumList.length === n) break;
        if(currentNum % 3 === 0 || String(currentNum).includes(3)) {
            currentNum++
            continue
        }
        
        villageNumList.push(currentNum)
        currentNum++;
        count--;
    }
    
    return villageNumList.pop()
}