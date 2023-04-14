function solution(numbers, k) {
    // 1. idx값은 2씩 건너뛴다.
    // 2. k를 count ++ 해주며 count === k 일때 공 가진사람 return
    // 3. (idx + 2) % numbers.length
    let throwMan = 0;
    let idx = 0
    for(let i = 0; i < k; i++) {
        throwMan = numbers[idx % numbers.length]
        idx += 2;
    }
    
    return throwMan
}