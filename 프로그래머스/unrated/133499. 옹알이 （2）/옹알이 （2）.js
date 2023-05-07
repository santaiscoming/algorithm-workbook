function solution(babbling) {
     const noRepeatRegExp = /(aya|ye|woo|ma)\1+/;
     const startRegExp = /^(aya|ye|woo|ma)+$/;

  return babbling.reduce((acc, word) => (
    !noRepeatRegExp.test(word) && startRegExp.test(word) ? acc += 1 : acc
  ), 0);
}