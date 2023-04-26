function solution(s) {
    // 항상 범위를 예외처리하고 시작하자
    if(s.length !== 4 && s.length !== 6) return false
    // 숫자가 아닌것을 찾아서 배열로 반환
    return !Array.isArray(s.match(/\D/g))
    
    // 원했던 풀이
//   let regex = /^\d{6}$|^\d{4}$/;
//   return regex.test(s);
}