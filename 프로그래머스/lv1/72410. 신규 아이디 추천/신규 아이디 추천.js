function solution(new_id) {
    var answer = '';
    let copy = new_id
    let regExp = /^[a-z0-9._-]+$/
    let removeDotRegExp = /\.{2,}/g
    // 1. 소문자로 전환
    copy = copy.toLowerCase()
    // 2. 소문자, 숫자, -, _, . 아닌것들 제외 -> filter
    copy = [...copy].filter((char) => regExp.test(char)).join('')
    // 3. . 2번이상 1개로 변경
    copy = copy.replace(removeDotRegExp, '.')
    // 4. . 이 처음과 끝이라면 제거
    if(copy[0] === '.') copy = [...copy].slice(1).join('')
    if(copy[copy.length - 1] === '.') copy = [...copy].slice(0, copy.length - 1).join('')
    // 5. 빈 문자열의 경우 new_id 길이만큼 a로 변경
    if(copy.length === 0) copy = 'a'
    // 6. new_id 길이가 16이상 -> 15개 + 마직에 . 있으면 제거
    if(copy.length > 15) {
        let modifyId = ''
        let idx = 0;
        while(modifyId.length < 15) {
            modifyId += copy[idx]
            idx += 1;
        }
        copy = modifyId
        if(copy[copy.length - 1] === '.') copy = copy.slice(0, copy.length - 1)
    }
    // 7. new_id 길이가 2글자 이하 -> 마지막 문자를 길이가 3될때까지 반복
    if(copy.length <= 2) {
        while(copy.length < 3) {
            copy += copy[copy.length - 1]
        }
    }
    return copy
}