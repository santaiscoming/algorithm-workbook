// n: 진법, t: result갯수, m: 인원, p: 나의 차례

function solution(n, t, m, p) {
    let result = '';
    let notationStr = '';
    
    // 1. 미리 구할 숫자의 갯수가 t개라고 하였다 -> t만큼 반복문을 돌면서 문자열을 만들어주자
    for(let i = 0; i <= t * m; i++) {
        notationStr += i.toString(n)
    }
    
    // 문자열을 돌면서 내 차례 즉 m 배수의 i번째 자리수를 result에 넣어주자
    for(let i = p - 1; i < notationStr.length; i += m){
        if(result.length === t) break;
        
        result += notationStr[i];
    }
    
    return result.toUpperCase()
}