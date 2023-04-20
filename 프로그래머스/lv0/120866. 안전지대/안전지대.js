function solution(board) {
    // lv.2 경로문제.. -> 방향키 쓰자
  const newlist = [];
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === 1) {
        newlist.push([i, j]);
      }
    }
  }
  let answer = newlist.length;
  for (let n of newlist) {
    for (let i of [-1, 0, 1]) {
      for (let j of [-1, 0, 1]) {
          // 멍청하게 맵 밖으로 나가지 않았다면
        if (0 <= n[0] + i && n[0] + i < board.length &&
            0 <= n[1] + j && n[1] + j < board[0].length) {
            // 멀쩡한 지역이구나
          if (board[n[0] + i][n[1] + j] === 0) {
              //방문표시
            board[n[0] + i][n[1] + j] = 1;
            answer++;
          }
        }
      }
    }
  }
    // 정사각형
  return board.length ** 2 - answer;
}

// 원하던 풀이
// function solution(board) {

//     let outside = [[-1,0], [-1,-1], [-1,1], [0,-1],[0,1],[1,0], [1,-1], [1,1]];
//     let safezone = 0;

//     board.forEach((row, y, self) => row.forEach((it, x) => {
//         if (it === 1) return false;
//         return outside.some(([oy, ox]) => !!self[oy + y]?.[ox + x])
//                ? false : safezone++;
//     }));

//     return safezone;
// }