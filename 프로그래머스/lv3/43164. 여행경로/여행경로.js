function solution(tickets) {
    // tickets를 탐색하자
        // [start, end] -> ticket
        // start == 인천, 
            // 다음 dfs에서는 end와 start가 같으면 dfs
             // result -> push(start를)
        // visited 가 필요하다
    // 언제 return해줘야하지 ?]
        // -> depth === tickets.length (+ 1 보류)
    const result = [];
    const visited = Array.from({length : tickets.length}, () => false);
    const depth = 0;
    
    const dfs = (path, depth) => {
        // 1. 종료 구문
        if(depth === tickets.length) {
            result.push(path)
            return;
        }
        depth += 1;
        // 2. 언제 result에 추가해줄래 ?
        tickets.forEach((ticket, idx) => {
            const [start, end] = ticket
            if(visited[idx]) return;
            if(start === path[path.length - 1]) {
                visited[idx] = true;
                dfs([...path, end], depth, visited)
                visited[idx] = false;
            }
        })
    }
    
    
    dfs(["ICN"], depth)
    
    return result.sort()[0]
}