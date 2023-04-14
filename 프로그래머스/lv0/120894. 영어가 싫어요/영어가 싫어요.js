function solution(numbers) {
  let answer = [];
  const numbersArr = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  const numbersObj = numbersArr.reduce((acc, cur, idx) => {
    acc[cur] = idx;
    return acc;
  }, {});

  let word = "";
  let oneWordArr = [...numbers];

  while (oneWordArr.length > 0) {
    word += oneWordArr.splice(0, 1);

    if (!!numbersObj[word] || numbersObj[word] === 0) {
      answer.push(numbersObj[word]);
      word = "";
    }
  }

  return Number(answer.join(""));
}
