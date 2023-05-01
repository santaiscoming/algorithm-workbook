function solution(progresses, speeds) {
  const answer = [];

  while (progresses.length > 0) {
    let cnt = 0;

    while (progresses.length > 0 && progresses[0] >= 100) {
      cnt++;
      progresses.shift();
      speeds.shift();
    }

    progresses = progresses.map((progress, index) => progress + speeds[index]);

    if (cnt > 0) {
      answer.push(cnt);
    }
  }
  return answer;
}
