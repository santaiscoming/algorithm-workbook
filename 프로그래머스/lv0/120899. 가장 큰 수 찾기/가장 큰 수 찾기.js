function solution(array) {
    const max = Math.max(...array)
    const maxIdx = array.indexOf(Math.max(...array))
    
    return [max, maxIdx]
}