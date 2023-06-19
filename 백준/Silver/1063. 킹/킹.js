const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const location = input[0].split(" ").slice(0, 2);
const moves = input.slice(1);
const xAxisMap = {
  A: 1,
  B: 2,
  C: 3,
  D: 4,
  E: 5,
  F: 6,
  G: 7,
  H: 8,
};

const reverseAxisMap = {
  1: "A",
  2: "B",
  3: "C",
  4: "D",
  5: "E",
  6: "F",
  7: "G",
  8: "H",
};

const direction = {
  R: [0, 1],
  L: [0, -1],
  B: [-1, 0],
  T: [1, 0],
  RT: [1, 1],
  LT: [1, -1],
  RB: [-1, 1],
  LB: [-1, -1],
};

let [king, stone] = location.map((str) => {
  return [...str].reverse().map((val, idx) => {
    if (idx === 1) return xAxisMap[val];
    return Number(val);
  });
});

// king = king.map((num, idx) => {
//   if(idx )
//   Math.abs(num - 8)
// });
// stone = stone.map((num) => Math.abs(num - 8));

const sameLocation = (arr1, arr2) => {
  return arr1.every((val, idx) => val === arr2[idx]);
};

const outChessMap = (arr1, arr2) => {
  return !(
    arr1.every((axis) => axis > 0 && axis < 9) &&
    arr2.every((axis) => axis > 0 && axis < 9)
  );
};

const updateHorse = (horse, dir) => {
  return horse.map((axis, idx) => Number(axis) + direction[dir][idx]);
};

// move를 돌면서 king 위치 업데이트
// if : sameLocation -> 돌도 king과 같은 방향으로 위치 업데이트
// if : outChessMap -> continue

for (let move of moves) {
  let copyKing = [...king];
  let copyStone = [...stone];
  let movedir = direction[move];

  copyKing = updateHorse(copyKing, move);

  if (outChessMap(copyStone, copyKing)) continue;
  if (sameLocation(copyKing, copyStone)) {
    copyStone = updateHorse(copyStone, move);
    if (outChessMap(copyStone, copyKing)) continue;
  }
  king = copyKing;
  stone = copyStone;
}

king = king
  .reverse()
  .map((num, idx) => {
    if (idx === 0) return reverseAxisMap[num];
    return num;
  })
  .join("");
stone = stone
  .reverse()
  .map((num, idx) => {
    if (idx === 0) return reverseAxisMap[num];
    return num;
  })
  .join("");
console.log(king);
console.log(stone);

// 맵은 A - H, 1 - 8 까지 한정됨 -> 0, 0 은 사용하지 않겠다.
// stone과 king의 Location 저장해야함
// direction 설정
// 예외처리
// 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다
// 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다
// 마지막에 reverse()
