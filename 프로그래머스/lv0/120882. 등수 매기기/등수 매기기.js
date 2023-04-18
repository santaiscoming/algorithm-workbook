function solution(score) {
    const averageArr = score.map((student) =>  (student[0] + student[1]) / student.length);
    
    // sort는 원본배열이 훼손된다.
    const sortAverage = [...averageArr].sort((a, b) => b - a);
    
    return averageArr.map((student) => sortAverage.indexOf(student) + 1);
}