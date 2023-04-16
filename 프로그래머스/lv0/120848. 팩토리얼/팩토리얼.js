const factorial = (n) => {
    if(n === 1 ) return 1;
    
    return n * factorial(n - 1);
}

function solution(n) {
    let num = 1;
    
    while(true) {
        if(factorial(num) > n) break;
        
        num += 1;
    }
    
    return num - 1
}