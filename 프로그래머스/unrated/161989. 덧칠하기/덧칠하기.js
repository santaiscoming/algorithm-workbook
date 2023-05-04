function solution(n, m, section) {
    let answer = 0;

    let complete = 0;

    section.forEach((wall) => {
        if (complete > n) return answer
        if (wall > complete) {
           complete = wall + m - 1;
           answer += 1;
         }
    });

  return answer;
}