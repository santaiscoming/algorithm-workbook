function solution(quiz) {
    // 좌항 : 식계산
    // 우항 : 같은지 확인
    
    return quiz.map((str) => str.split(' = '))
                    .map(([left, right]) =>  eval(left) === Number(right) ? 'O' : 'X')
}