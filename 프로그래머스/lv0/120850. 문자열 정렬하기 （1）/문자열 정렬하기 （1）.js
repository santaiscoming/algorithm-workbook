function solution(my_string) {
                        // isNaN을 사용하면 '2'도 숫자로 인식하기에 Number.isNaN사용
    return [...my_string].filter((str) => !Number.isNaN(Number(str)))
                        // 각각의 문자타입의 숫자를 숫자타입으로 안바꿔주면 fail
                         .map((str) => Number(str))
                         .sort((a, b) => a - b)
    
    const regExp = /\d/g
                        // match 메서드는 일치하는 문자열을 반환하고 없으면 null 반환
                        // 그렇다는 뜻은 1,2,2,3,9 라는 값이 truthy한 값이기에 true로 평가되는것이지 실제로 true를 반환하지 않으니 !! 부정연산자를 이용해 true값으로 변환
    return [...my_string].filter((str) => !!str.match(regExp))
                         .map((str) => Number(str))
                         .sort((a, b) => a - b)
}