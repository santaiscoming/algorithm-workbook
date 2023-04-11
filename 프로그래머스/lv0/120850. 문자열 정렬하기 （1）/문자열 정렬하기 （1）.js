function solution(my_string) {
                        // isNaN을 사용하면 '2'도 숫자로 인식하기에 Number.isNaN사용
    return [...my_string].filter((str) => !Number.isNaN(Number(str)))
                        // 각각의 문자타입의 숫자를 숫자타입으로 안바꿔주면 fail
                         .map((str) => Number(str))
                         .sort((a, b) => a - b)
}