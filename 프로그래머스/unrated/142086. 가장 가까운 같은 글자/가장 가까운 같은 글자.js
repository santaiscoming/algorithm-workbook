function solution(s) {
    // s를 돌면서 char를 mapping 해주자
        // map에 없으면 -> 해당 char 위치를 저장 key : {idx : x}
            // answer에 -1 push
        // 있으면 현재 char의 idx - map.char.idx 뺴주고
            // answer에 뺴준값 push
            // map.char.idx = 현재 char idx 덮기
    
    const strMap = {};
    const result = [];
    
    const map = [...s].reduce((map, char, idx) => {
        if(!map[char]) {
            map[char] = { idx }
            result.push(-1)
            return map
        }
        result.push(idx - map[char]['idx'])
        map[char]['idx'] = idx
        return map
    }, {})

    return result
    
    
  //   [...s].map((char, i) => {
  //   const count = s.slice(0, i).lastIndexOf(char);
  //   return count < 0 ? count : i - count;
  // })
}