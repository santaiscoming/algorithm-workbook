function solution(my_string) {
    
    let result = 0;
    let str = my_string.split(' ')
    
    // 1. str 배열을 돌면서 숫자일때 stack에 넣어준다
        // 1-1. + 일때 : 초기값과 다음인덱스의 숫자를 더해준다
        // 1-2 - 일때 : 초기값과 다음인덱스의 숫자를 빼줌
    str = str.map((num) => {
        if(!Number.isNaN(Number(num))) return Number(num);
        return num
    })
    
    for(let i = 0; i < str.length; i++) {
        if(i === 0) result += str[i]
        
        if(str[i] === '+') result += str[i + 1];
        if(str[i] === '-') result -= str[i + 1]
        
    }
    
    return result
}