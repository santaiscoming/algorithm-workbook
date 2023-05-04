function solution(lottos, win_nums) {
    // 0의 개수만큼 ++, -- : 최고, 최소

    const lottoMap = Array.from({length : 6}, (_, idx) => idx + 1)
                          .reduce((map, curr) => {
                              map[curr] = 7 - curr;
                              return map;
                          }, {})
    console.log(lottoMap)
    const correctNumberCount = lottos.filter((lotto) => win_nums.includes(lotto)).length
    const zeroCount = lottos.filter((lotto) => !lotto).length
    const winCount = correctNumberCount + zeroCount
    if(winCount === 0) return [lottoMap['1'], lottoMap['1']]
    if(correctNumberCount === 0) return [lottoMap[winCount], lottoMap['1']]
    return [lottoMap[winCount], lottoMap[correctNumberCount]];
}