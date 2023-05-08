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
      console.log(firstChar)
    if (!firstChar) firstChar = s[i]
    if (firstChar === s[i]) {
      sameCount += 1
    } else {
      notSameCount += 1
    }
    if (sameCount === notSameCount) {
      result += 1
      sameCount = 0
      notSameCount = 0
      firstChar = ''
    }
      console.log(firstChar)
  }
  if(firstChar) result += 1;
  return result
}
