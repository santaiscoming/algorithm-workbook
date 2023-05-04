function solution(k, m, score) {
    // m : 한상자에 들어갈 사과 개수
    // p : 가장 낮은 점수 사과
    // k : 가장 높은 점수 사과
    // 사과 한상자 가격 : p * m
    
    // 내림차순으로 정렬후 m개씩 넣어준다 -> arr
    // 해당 상자의 가격은 최솟값(Math.min(arr)) * 한상자에 들어간 사과 개수 (m)
        // if 상자.length < m : 못팜
    let result = 0;
    score.sort((a, b) => b - a)
    
    for(let i = m-1; i < score.length; i += m){
        result += score[i] * m;
    }

    
    return result
}