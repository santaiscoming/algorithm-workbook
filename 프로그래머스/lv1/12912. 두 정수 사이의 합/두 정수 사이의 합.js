function solution(a, b) {
    const arr = [a, b].sort((a, b) => b - a)
    let result = 0;
    
    for(let i = Math.min(...arr); i <= Math.max(...arr); i++) {
        result += i
    }
    
    return result
}