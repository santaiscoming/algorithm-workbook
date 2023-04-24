// 문자열 앞에 + 붙이면 숫자타입으로 형변환 하듯이 - 붙이면 음수로 형변환

function solution(absolutes, signs) {
    return absolutes.map((num, idx) => signs[idx] ? +num : -num)
                    .reduce((acc, cur) => acc + cur, 0)
}   