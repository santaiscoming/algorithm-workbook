function solution(my_string) {
    // pattern이 정규식이면 전역(g) 플래그가 설정되어 있어야 합니다. 그렇지 않으면 TypeError가 발생합니다.
    // -> 전역 플래그가 없으면 첫번째로 매칭되는 패턴만 대체되기 때문
    const reg = /[aeiou]/g
    return my_string.replaceAll(reg, '');
}