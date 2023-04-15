function solution(my_str, n) {
    const result = [];
    const my_strArr = [...my_str]
    
    while(true) {
        if(my_strArr.length === 0) break;
        
        result.push(my_strArr.splice(0, n).join(''))
    }
    return result
}