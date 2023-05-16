const bracketMap = {
    '[' : ']',
    '{' : '}',
    '(' : ')',
}

console.log(bracketMap['['])

const isCorrectBracket = (str) => {
        let strArr = [...str]
        const stack = [];
        
        while(strArr.length > 0) {
            const firstChar = strArr.shift()
            if(bracketMap[stack[stack.length - 1]] === firstChar) {
                stack.pop()
            } else {
                stack.push(firstChar)
            }
        }
        return !stack.length
    }

function solution(s) {
    let result = 0;
    let strArr = [...s]
    let count = s.length
    
    // 2가지 로직 필요
    // 1. 맨앞을 빼서 맨 뒤로 보내는 로직 -> 반복해야함 while : s.length 만큼 ++
    do {
        isCorrectBracket(strArr) ? result++ : ''
        strArr.push((strArr.shift()))
    } while (count-- > 1)
    
    return result
    // 2. 올바른 괄호 문자열인지 확인하는 로직
    
}