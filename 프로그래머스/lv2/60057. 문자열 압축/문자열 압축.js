const wordsSlice = (words, numberOfWord) => {
  let count = 0;
  const result = [];

  while (true) {
    if (count >= words.length) break;
    result.push([...words].splice(count, numberOfWord));
    count += numberOfWord;
  }

  return result.map(arr => arr.reduce((acc, cur) => acc + cur));
};

function solution(s) {
  if (s.length === 1) return 1;

  const compress = [];
  for (let i = 1; i <= s.length / 2; i++) {
    // map의 사이즈가 작은걸 계속 업데이트 후에 i값 Math.min?
    const slice = wordsSlice(s, i);
    let count = 1;
    const innercomp = [];

    for (let i = 1; i <= slice.length; i++) {
      if (slice[i] === slice[i - 1]) {
        count += 1;
        continue;
      }
      if (count > 1) {
        innercomp.push(count);
        innercomp.push(slice[i - 1]);
        count = 1;
        continue;
      }
      innercomp.push(slice[i - 1]);
    }
    compress.push(innercomp.join(''));
  }

  return Math.min(...compress.map(str => str.length));
}
