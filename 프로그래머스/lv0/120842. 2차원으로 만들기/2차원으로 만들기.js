function solution(num_list, n) {
    var answer = [];
    // n개만큼의 배열을 넣어주자
    for(let i = 0; i < num_list.length / n; i++) {
        answer.push([])
    }

    let count = 0;
    while(num_list.length > 0 && count < answer.length) {
        for(let i = 0; i < n; i++) {
            answer[count].push(num_list.shift())
        }
        count += 1;
    }
    
    return answer
}