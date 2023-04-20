// 수열의 등차가 1인것을 이용 + 중간값
// function solution(num, total) {
//     var min = Math.ceil(total/num - Math.floor(num/2));
//     var max = Math.floor(total/num + Math.floor(num/2));

//     return new Array(max-min+1).fill(0).map((el,i)=>{return i+min;});
// }

function solution(num, total) {
  let answer = Array.from({ length: num }, () => 0);
  // 처음에는 범위를 -total 만큼만 했는데 error -> 범위문제?
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

