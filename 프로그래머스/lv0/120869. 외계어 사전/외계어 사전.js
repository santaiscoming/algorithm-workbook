function solution(spell, dic) {
  // dic 배열을 돌면서 각 문자열의 출몰 빈도 계산
  for (let str of dic) {
    const map = [...str].reduce((acc, cur) => {
        acc[cur] = (acc[cur] || 0) + 1
        return acc
    }, {});
      
    const strFrequency = [...Object.keys(map)];
      
    const spellIncludes = strFrequency.filter((char) => [...spell].includes(char))
    
    if(spellIncludes.length === spell.length) return 1;
      // 출몰의 키값에 spell 만으로 형성되어있으면 count ++
  }
    
    return 2;
}
