// 0을 제거하고 제거한 0의 개수륿 반환하는 함수
const removeZero = (num) => {
        let strArr = [...String(num)].map((char) => Number(char))
        let zeroCount = 0;
        let result = ''
        strArr.forEach(char => {
            if(!char) zeroCount++;
            if(char) result += char
        })
        return [zeroCount, result]
    }

function solution(s) {
    let zeroCount = 0;
    let convertBinaryCount = 0
    
    // 0을 제거한 길이에 대해 이진 변환 하는 로직
    while(true) {
        let [count, removeZeroNum] = removeZero(s)
        zeroCount += count;
        s = (removeZeroNum.length).toString(2)
        convertBinaryCount++;
        if(s == 1) break
    }
    
    return [convertBinaryCount, zeroCount]
}