const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M, S] = input;

// 스택에 넣고 뒤부터 짜르면서 찾자
let findIOI = "I";

Array.from({ length: N }, () => {
  findIOI += "OI";
});

const stack = [];
let count = 0;

for (let i = 0; i < M; i++) {
  stack.push(S[i]);

  let curStr = stack.slice(-findIOI.length).join("");
  if (curStr === findIOI) count++;
}

console.log(count);