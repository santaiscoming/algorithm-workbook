function solution(n, lost, reserve) {

  const students = Array.from({length : n}, () => 1);

  lost.forEach((num) => {
    students[num - 1]--;
  });

  reserve.forEach((num) => {
    students[num - 1]++;
  });

  students.forEach((uniform, idx) => {
    if (uniform === 0) {
      if (students[idx - 1] === 2) {
        students[idx] += 1;
        students[idx - 1] -= 1;
      } else if (students[idx + 1] === 2) {
        students[idx] += 1;
        students[idx + 1] -= 1;
      }
    }
  });

  return students.filter((uniform) => uniform >= 1).length;
}
