function solution(survey, choices) {
    const mbti = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]];
    const mbtiMap = mbti.reduce((acc, [left, right]) => ({...acc, [left]: 0, [right]: 0}), {});
    
    
    console.log(mbtiMap)
    
    for (let i = 0; i < survey.length; i++) {
        const score = choices[i] - 4;
        const key = score > 0 ? survey[i][1] : survey[i][0];
        mbtiMap[key] += Math.abs(score);
    }

    const result = mbti.map(([a, b]) => mbtiMap[a] >= mbtiMap[b] ? a : b);
    
    return result.join('');
}