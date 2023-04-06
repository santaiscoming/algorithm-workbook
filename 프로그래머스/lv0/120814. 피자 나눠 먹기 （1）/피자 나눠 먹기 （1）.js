function solution(n) {
    // var answer = 1;
    // while(n > 0) {
    //     n -= 1;
    //     if (n === 0) break;
    //     if (n % 7 === 0) answer += 1;
    // }
    // return answer;
    
    return n % 7 === 0 ? n / 7 : Math.ceil(n / 7)
}