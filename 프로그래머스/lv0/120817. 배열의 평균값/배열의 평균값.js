function solution(numbers) {
     const sumAv = numbers.reduce((acc, cur) => acc + cur, 0) / numbers.length;
    
    return sumAv.toFixed(1)
}