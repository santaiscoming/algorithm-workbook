const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = input[0];
const peopleMemory = input.slice(1).join("").split(" ").map(Number);

const result = Array.from({ length: N }, () => false);

// 보기로 주어진 왼쪽에 몇명이 있는지 배열을 각각 돌자
// 2차원 배열로 돌것이기에 outer 반복문을 돌때 idx는 현재의 사람을 위치를 잡아주는중
// inner반복문을 돌면서 count++ 해준다
// 해당 카운터가 outer의 큰사람 memory와 일치하고 내 자리가 false 즉, 할당되지 않았다면 그곳이 내자리
// 키가 작은사람이 먼저 자리를 잡기때문에 키 큰 사람은 왼쪽에 같은 사람이 있어도 작은 사람이 먼저 자리를 차지함

for (let i = 0; i < peopleMemory.length; i++) {
  // 내 앞에 사람들이 몇명있는지 주어진 값과 같을때까지 ++
  let count = 0;
  for (let j = 0; j < peopleMemory.length; j++) {
    // 현재 들어갈 자리에 사람이 없고, 내앞에 사람의 count가 동일할때 그게 내자리
    if (result[j] === false && count === peopleMemory[i]) {
      result[j] = i + 1;
      break;
    }

    if (result[j] === false) {
      count++;
      continue;
    }
  }
}

console.log(result.join(" "));
