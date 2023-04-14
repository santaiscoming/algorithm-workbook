function solution(numbers, target) {
    // [1, 1, 1, 1, 1] 기준
    // 1. numbers를 돌면서 가지치기 해주자
        // 1-1 dfs다 각 number마다 +1, -1 해줘야겠어
            //1-1-1. 그렇다면 배열을 돌때까지 sum을 누적해야겠군
            //1-1-2. 근데 각 재귀를 돌면서 sum은 어떻게 접근해?
                // 1. 전역변수로 선언하자 -> 그렇다면 다른 재귀가 돌때도 sum값을 참조해서 안된다
                // 2. parameter로 넘겨주자
        // 1-2 언제멈추지 ? => numbers를 모두 돌았을때 (index가 numbers.length 일때)
    // 2. 배열을 다돌았다. -> target과 다 돌은값(더하거나 뺀값)이 같이면 result ++
    let result = 0
    let idx = 0;
    
    // 재귀를 부를때마다 numbers를 돌때까지 더해주거나 뺀값을 전달해야겠어 -> sum
    // base cose : 배열이 다 돌았는지는 어떻게알지? -> index를 만들어주자
    const dfs = (sum, idx) => {
        //base code: 어? 근데 배열끝까지 돌고나서 target과 같은지 비교해야겠네
        if(idx === numbers.length) {
            if(sum === target) result += 1;
            return
        }
        
        dfs(sum + numbers[idx], idx + 1)
        dfs(sum - numbers[idx], idx + 1)
    }
    
    dfs(0, 0)
    
    return result
}
                    // dfs +1                      dfs -1
//                     +1,           |           -1
//               +1           -1     |    +1            -1
//            +1   -1       +1   -1  |  +1   -1       +1   -1 