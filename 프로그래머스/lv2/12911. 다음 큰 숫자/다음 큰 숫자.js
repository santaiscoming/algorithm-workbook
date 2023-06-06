function solution(n) {
  let compareNum = n + 1;
  let sameOneCount = countOnes(n.toString(2));

  while (true) {
    let compareNumCount = countOnes(compareNum.toString(2));

    if (sameOneCount === compareNumCount) {
      return compareNum;
    }

    compareNum++;
  }
}

function countOnes(binaryNum) {
  let count = 0;
  for (let i = 0; i < binaryNum.length; i++) {
    if (binaryNum[i] === '1') {
      count++;
    }
  }
  return count;
}