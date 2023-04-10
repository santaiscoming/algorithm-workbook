function solution(answer) {
  const students = [
    [1, [1, 2, 3, 4, 5]],
    [2, [2, 1, 2, 3, 2, 4, 2, 5]],
    [3, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]],
  ];

  const result = students.map(([name, stdAnswer]) => [
    name,
    answer.filter((val, idx) => val === stdAnswer[idx % stdAnswer.length])
      .length,
  ]);

  const mostRightAnswer = Math.max(...result.map(([_, stdRightAnswer]) => stdRightAnswer));

  return result
    .filter((arr) => arr[1] === mostRightAnswer)
    .map((arr) => arr[0]);
}
