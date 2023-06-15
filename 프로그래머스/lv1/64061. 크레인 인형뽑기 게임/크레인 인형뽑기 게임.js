// 1. moves를 돌면서 해당 위치에서 0이 아닌값을 찾습니다.

// 2-1   1에서 찾은값과 stack의 가장 마지막값이 같은경우 cnt해주고 stack에서 삭제합니다.
// 2-2   1에서 찾은값과 stack의 가장 마지막값이 다른경우 stack에 push합니다.
// 2-3   1에서 찾은값을 0으로 바꿔줍니다. 

// 3. 총 cnt한 개수 * 2 를 출력해줍니다.


// [ -> [ y : 4, x : 0 ]
//   [0, 0, 0, 0, 0],
//   [0, 0, 1, 0, 3],
//   [0, 2, 5, 0, 1],
//   [4, 2, 4, 4, 2],
//   [3, 5, 1, 3, 1],
// ];


// 1번부터 moves : 1 5 3 5 1 2 1 4 
// 0번부터 moves : 0 4 2 4 0 1 0 3 

// [
//   [0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0],
//   [0, 0, 5, 0, 0],
//   [0, 2, 4, 0, 2],
//   [0, 5, 1, 3, 1],
// ];

// 4311324
// 424
// 11, 33 => 총 4개 

function solution(board, moves) {
    let stack = [];
    let cnt = 0;

        
    moves.forEach((item)=>{
        let cur = item-1;
        
        for(let j=0; j<board.length; j++){
            let pick = board[j][cur];
            
            if(pick!==0){
                if(stack[stack.length-1] === pick){
                    stack.pop();
                    cnt++;  
                }else{
                    stack.push(pick);
                }
                
                board[j][cur] = 0;
                break;
            }
        }
    })
    return cnt*2;
}