function solution(brown, yellow) {
    // 패턴이 보이는 문제같다 패턴을 찾자
    // 1. pattern : 
    // 총 카펫의 수 : brown + yellow
    // yellow 카펫 : 총 카펫 배열 [x, y]에서 (x - 2) * (y - 2)
    
    // 2. 그렇다면 총 카펫의 개수(12 ,9, 48)과 같은 x, y 경우의 수를 만들자
    const carpetCases = [];
    const carpetSize = brown + yellow
    
    for(let i = 1; i <= carpetSize; i++) {
         for (let j = 1; j <= i; j++) {
            if(i * j > carpetSize) break;
            if(j * i === carpetSize) carpetCases.push([i, j]) ;
       }
    };
    console.log(carpetCases)
    
    // 3. (2)에서 만든 모든 경우의 수에서 yellow(인수로 받음) 카펫의 개수와 같은 배열을 찾자
    const result = [];
    
    for(let i = 0; i < carpetCases.length; i++) {
        const yellowCarpet = (carpetCases[i][0] - 2) * (carpetCases[i][1] - 2)
        if(yellow === yellowCarpet) result.push(carpetCases[i])
    }
    
    return result.flat()
}