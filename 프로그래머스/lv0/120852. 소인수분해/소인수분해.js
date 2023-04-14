function solution(n) {
    var answer = [];
    let count = 2;
    
    while (n > 1) {
        if(n % count === 0) {
            n /= count
            answer.push(count)
        } else {
            count += 1;
        }
    }
    
    return [...new Set(answer)]
}