// (x, y) 위치에 key를 board에 부착하는 함수
function attach(x, y, M, key, board) {
    for (let i = 0; i < M; i++) {
        for (let j = 0; j < M; j++) {
            board[x+i][y+j] += key[i][j];
        }
    }
}

// (x, y) 위치에서 key를 board에서 제거하는 함수
function detach(x, y, M, key, board) {
    for (let i = 0; i < M; i++) {
        for (let j = 0; j < M; j++) {
            board[x+i][y+j] -= key[i][j];
        }
    }
}

// 배열을 90도 회전하는 함수
function rotate90(arr) {
    return arr[0].map((value, index) => arr.map(row => row[index])).reverse();
}

// 자물쇠가 올바르게 잠겨있는지 확인하는 함수
function check(board, M, N) {
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (board[M+i][M+j] !== 1) {
                return false;
            }
        }
    }
    return true;
}

// 주어진 key와 lock을 이용해 잠금 해제가 가능한지 판단하는 함수
function solution(key, lock) {
    let M = key.length;
    let N = lock.length;

    // 크기가 (M*2 + N)인 2차원 배열 board 생성
    let board = Array.from({length: M * 2 + N}, () => Array(M * 2 + N).fill(0));
    
    // 자물쇠 중앙에 배치
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            board[M+i][M+j] = lock[i][j];
        }
    }
    /*
    	[
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

    */

    let rotatedKey = key;
    // 모든 방향으로 시도 (4번 반복)
    for (let r = 0; r < 4; r++) {
        rotatedKey = rotate90(rotatedKey);
        for (let x = 0; x < M + N; x++) {
            
            for (let y = 0; y < M + N; y++) {
                // 열쇠를 넣어봅니다
                attach(x, y, M, rotatedKey, board);
                // lock 가능한지 확인
                if (check(board, M, N)) {
                    return true;
                }
                // 열쇠를 제거합니다
                detach(x, y, M, rotatedKey, board);
            }
        }
    }
    
    return false;
}