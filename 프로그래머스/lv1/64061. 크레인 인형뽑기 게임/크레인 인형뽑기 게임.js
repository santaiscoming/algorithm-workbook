function solution(board, moves) {
    // 행렬을 뒤집고 move[i] 의 행렬에서 0이 아닐떄까지 들어가자
    const newMap = Array.from({length : board.length}, () => [])
    const result = [];
    let count = 0;
    
    for(let i = 0; i < board.length; i++) {
        for(let j = 0; j <board.length; j++) {
            if(board[j][i]) newMap[i].push(board[j][i])
        }
    }
    
    moves.forEach((move, idx) => {
        let resultLast = result[result.length - 1]
        let curKakao = newMap[move - 1].shift()
        if(!curKakao) return

        // console.log(`mve : ${move}, last : ${resultLast}, cur : ${curKakao}, result : ${result}`)
        if(curKakao === resultLast) {
            count += 2;
            result.splice(-1)
        } else {
            result.push(curKakao)
        }

    })
    
    return count
}