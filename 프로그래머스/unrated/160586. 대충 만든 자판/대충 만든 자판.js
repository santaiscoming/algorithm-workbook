function solution(keymap, targets) {
  const answer = [];
  const keyMap = {};
    // 키맵의 각 키(자판?)의 최소 클릭횟수를 맵으로 만들어주자
    keymap.forEach((key) => {
        for (let i = 0; i < key.length; i++) {
            if (keyMap[key[i]]) {
                // 이미 매핑된것과 현재 키를 도는 인덱스값을 비교해서 작은값을 넣어주면 최소값
            const idx = Math.min(i + 1, keyMap[key[i]]);
            keyMap[key[i]] = idx;
            } else {
                // 키의 시작은 1부터니까
              keyMap[key[i]] = i + 1
            }
        }
    })
    console.log(keyMap)
    
    for (const target of targets) {
      let count = 0;
      for (let i = 0; i < target.length; i++) {
        count += keyMap[target[i]];
       }
    // count가 있으면 넣고 없으면 -1
        answer.push(count || -1);
    }
  return answer;
}