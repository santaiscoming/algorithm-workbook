const isEven = (num) => {
    return !(num % 2) 
}

function solution(num) {
    let count = 0;
    let number = num
    
    while(count <= 500) {
        if(number === 1) return count
        count += 1;
        if(isEven(number)) {
            number /= 2;
            continue;
        }
        if(!isEven(number)) number = (number * 3) + 1;
        
    }
    
    return -1;
}