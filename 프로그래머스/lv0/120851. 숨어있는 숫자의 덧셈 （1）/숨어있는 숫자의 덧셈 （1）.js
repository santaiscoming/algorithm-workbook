function solution(my_string) {
  // const regExp = /[0-9]/g 왜안돼지..?
  return [...my_string]
    .filter((str) => !isNaN(str))
    .reduce((acc, cur) => Number(acc) + Number(cur));
}