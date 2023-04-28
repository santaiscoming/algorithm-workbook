
function solution(genres, plays) {
  const playMap = {}
  const result = [];
  const genresMap = genres.reduce((acc, cur, idx) => {
      acc.get(cur) ? acc.set(cur, acc.get(cur) + plays[idx]) : acc.set(cur, plays[idx])
      return acc
  }, new Map())
    // 가장 많이 재생된 장르 구하기
    // 장르별 플레이 횟수 저장할 객체 만들기 (정렬시키자)
    // 2곡만 선택가능하다 count 변수를 만들어 ++
        // 해당곡의 play 횟수가 1개 이상일땐 plays의 idx값이 작은것을 넣어줘라 (예외처리)
    const sortGenreMap = new Map([...genresMap.entries()].sort((a, b) => b[1] - a[1]))
    // while문을 돌면서 [...sortGenreMap.keys()] 로 탐색
    
    genres.forEach((genre, idx) => {
        if(!playMap[genre]) {
            playMap[genre] = [];
            playMap[genre].push([plays[idx], idx])
            return;
        }
            playMap[genre].push([plays[idx], idx])
    })
    Object.values(playMap).forEach((arr) => {
        arr.sort((a, b) => b[0] - a[0])
    })
    let sortGenreMapKeys = [...sortGenreMap.keys()]
    sortGenreMapKeys.forEach((genre) => {
        playMap[genre].forEach((arr, idx) => {
            if(idx > 1) return
            const [play, num] = arr
            result.push(num)
            
        })
    })
    
    return result
  }