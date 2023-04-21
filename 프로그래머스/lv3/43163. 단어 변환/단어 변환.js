    // 일단 돌아가게 만들어라
function solution(begin, target, words) {
    // 한글자가 다르면 배열의 해당 값으로 변경해
        // 변경할때마다 count++;
    // dfs parameter
        // 1. 현재단어가 뭘까
        // 2. 뎁스
        // 3. 원본배열(변경해야된다 ?)
    // 방문처리
    // 타겟이랑 같아지면 L 를 배열에 넣어
    const resultArr = [];

    const visited = Array.from({length : words.length}, () => false)

    const dfs = (begin, L) => {
            if(begin === target) {
                resultArr.push(L)
                return;
            }
        for(let i = 0; i < words.length; i++) {
            if(diffOneWord(begin, words[i]) && !visited[i]) { 
                visited[i] = true;
                console.log(begin, visited)  
                dfs(words[i], L + 1)
                visited[i] = false;
            }
        }
    }
    
    
    dfs(begin, 0)
    
    return resultArr.length > 0 ? Math.min(...resultArr) : 0
}
    
    const diffOneWord = (word1, word2) => {
        let count = 0;
        [...word1].forEach((str, idx) => {
            if(str !== word2[idx]) count++;
        })
        
       return count === 1 ? true : false;
    }