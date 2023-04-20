// const sumArr = (arr) => {
//     return arr.reduce((acc, cur) => acc + cur, 0)
// }

// function solution(num, total) {
//     // num의 범위가 100까지니까
//     const numArr = Array.from({length : 100}, (_, idx) => idx + 1)
//     let idx = 0;
//     let negative = -1;
//     const sliceArr = numArr.slice(idx, idx + num)
    
//     while(true) {
//         if(sumArr(sliceArr) === total) return sliceArr
//         if(sumArr(sliceArr) < total) {
//             idx += 1;
//             continue
//         } else {
//             sliceArr.pop()
//             sliceArr.shift(sliceArr[0] - 1)
//             negative -= 1;
//             continue;
//         }  
//     }
// }

function solution(num, total) {
  let answer = Array.from({ length: num }, () => 0);
  //
  for (let i = -(total + num); i <= total + num; i++) {
    let sum = 0;
    let index = 0;
    answer = Array.from({ length: num }, () => 0);
    for (let j = i; j < i + num; j++) {
      sum += j;
      answer[index++] = j;
    }
    if (sum === total) return answer;
  }
}

