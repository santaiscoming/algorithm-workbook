const rotate = (key) => {
    const newkey = Array.from({length : key.length}, () => Array.from({length : key.length}, () => 0))
    for(let i = 0; i < newkey.length; i++){
        for(let j = 0; j < newkey.length; j++){
            newkey[i][j] = key[key.length - j - 1][i]
        }
    }
    return newkey 
}

function solution(key, lock) {
    // key를 회전하는 로직 2, 1 -> 1, 2
    [[0, 0, 0],
     [1, 0, 0], 
     [0, 1, 1]]
    [[ 0, 1, 0 ],
     [ 1, 0, 1 ], 
     [ 1, 1, 0 ] ]
    console.log(rotate(key))
    // 자물쇠의 범위를 새로 만들어야한다
        // 자물쇠의 끝부분만 맞을때 -> 키의 첫부분만 맞을 수 있음
        // 자물쇠의 첫부분만 맞을때 -> 키의 끝부분만 맞을 수 있음
         // x  x  x
         // x  x  x
         // x  x [1, 1, 1]
         //      [1, 1, 0]
         //      [1, 0, 1] x x 
         //             x  x x   
         //             x  x x   
}