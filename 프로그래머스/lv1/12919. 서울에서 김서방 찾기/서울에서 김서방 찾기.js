function solution(seoul) {
    
    // ES6에 추가된 findIndex(callback) 사용도 가능
    const idx = seoul.findIndex((element) => element === 'Kim')
    // const idx = seoul.indexOf('Kim')
    
    return `김서방은 ${idx}에 있다`
}