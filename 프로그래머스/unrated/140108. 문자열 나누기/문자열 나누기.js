function solution(s) {
  // 첫글자가 나온 횟수를 세자 -> firstCoumt
  // 첫글자가 아닌 횟수를 세자 -> notFirst
  // 증가하면서 같은경우를 찾자
  //while : length === count && firstCOunt !== notFirst
  // 잘라줄때 splice(0, firstCount)
  let result = 0
  let sameCount = 0
  let notSameCount = 0
  let firstChar = ''

  for (let i = 0; i < s.length; i++) {
    let curChar = s[i]
      // 우리가 돌아야할 문자의 0번째를 이니셜라이즈
    if (!firstChar) firstChar = curChar
    // 처음등장한 문자와 s[i] 가 같으면
    if (firstChar === curChar) sameCount += 1
    // 처음등장한 문자와 s[i] 가 같지않으면
    if (firstChar !== curChar) notSameCount += 1
    //  x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
    if (sameCount === notSameCount) {
      result += 1
      sameCount = 0
      notSameCount = 0
      firstChar = ''
    }
  }
     
  if(firstChar) result += 1;
  return result
}
