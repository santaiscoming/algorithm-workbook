function solution(numer1, denom1, numer2, denom2) {
  let ans = [];
  let maxCommon;
  let 분자 = denom1 * numer2 + denom2 * numer1;
  ans.push(분자);
  let 분모 = denom1 * denom2;
  ans.push(분모); //8
    // 최대공약수를 구해보자 -> 분자와 분모의
     let ref = Math.max(분자, 분모)
    for(let i = ref; i > 0; i--) {
        // console.log({i, 분자, 분모})
        if(분자 % i === 0 && 분모 % i === 0) {
            maxCommon = i
            break;
        } 
    }
    
    return [분자 / maxCommon, 분모 / maxCommon]
    
    
  // //만약에 분자랑 분모가 계속 2로 나눌수 있다면 2로 나누어라
  // if (분자 % minMultiple === 0 && 분모 % minMultiple === 0) {
  //   분자 = 분자 / minMultiple;
  //   분모 = 분모 / minMultiple;
  //   let ans = [];
  //   ans.push(분자);
  //   ans.push(분모);
  //   console.log(분자, 분모);
  //   return ans;
  // }
  // console.log(ans);
  // return ans;
}
