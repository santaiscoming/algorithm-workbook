function solution(k, m, score) {
    // 사과 점수 정렬
    // 박스갯수만큼 반복
    let result = 0;
    score.sort((a, b) => b-a);   

    for(let i = 1; i <= Math.floor(score.length / m); i++) {
        result += score[m * i - 1] * m;
    }
    return  result;
}