const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [N, M] = input[0].split(" ");
let box = input.slice(1).map((num) => [...num]);
let max = Number.MIN_SAFE_INTEGER;

const isSameEdge = ({ topLeft, topRight, bottomLeft, bottomRight }) => {
  return new Set([topLeft, topRight, bottomLeft, bottomRight]).size === 1;
};

// 꼭지점 위치 : 생성한 사각형의 y축 0번째 끝,, x축 0번째, 끝

// 4 2 1 0 1
// 2 2 1 0 0
// 2 2 1 0 1

for (let y = 0; y < N; y++) {
  for (let x = 0; x < M; x++) {
    //각 꼭지점에서 정사각형 체크
    let count = 0;
    while (true) {
      if (y + count >= N) break;
      if (x + count >= M) break;
      const topLeft = box[y][x];
      const topRight = box[y][x + count];
      const bottomLeft = box[y + count][x];
      const bottomRight = box[y + count][x + count];
      const arr = [topLeft, topRight, bottomLeft, bottomRight];
      if (arr.some((el) => undefined)) break;
      if (isSameEdge({ topLeft, topRight, bottomLeft, bottomRight })) {
        max = Math.max(max, (count + 1) ** 2);
      }
      count++;
    }
  }
}

console.log(max);
