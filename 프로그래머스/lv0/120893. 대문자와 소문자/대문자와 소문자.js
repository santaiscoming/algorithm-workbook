function solution(my_string) {
    // ascii 코드로 변환 : str.charCodeAt()
    // utf 문자열로 변환 : String.fromCharCode(parameter)
    const convertAscii = [...my_string].map((str) => str.charCodeAt(0));
        // 대분자 아스키코드에 32를 더해주면 소문자가 된다 ex) A: 65 -> a: 97
    const reverseUpperLowerAscii = convertAscii.map((ascii) => {
        if(ascii >= 97) return ascii - 32;
        if(ascii >= 65) return ascii + 32;
    });
    
    const convertStr = reverseUpperLowerAscii.map((ascii) => String.fromCharCode(ascii)).join('')
    
    return convertStr
}