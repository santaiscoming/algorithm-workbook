function solution(num, k) {
    const findIdx = [...String(num)].indexOf(String(k))
    
    return Math.sign(findIdx) >= 0 ? findIdx + 1 : -1
}