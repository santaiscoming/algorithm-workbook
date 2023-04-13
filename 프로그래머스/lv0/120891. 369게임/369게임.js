function solution(order) {
    return [...String(order)].filter((num) => {
        if(Number(num) % 3 === 0 && Number(num) !== 0) return num;
           }).length;
    
}