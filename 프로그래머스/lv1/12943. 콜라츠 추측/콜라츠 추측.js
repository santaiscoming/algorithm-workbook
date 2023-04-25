const isEven = (num) => {
    return !(num % 2) 
}

function solution(num) {
    let count = 0;
    
    while(count <= 500) {
        if(num === 1) return count
        count += 1;
        if(isEven(num)) {
            num /= 2;
            continue;
        } 
        num = (num * 3) + 1;
    }
    
    return -1;
}