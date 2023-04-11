function solution(cipher, code) {
    // filter의 index는 0부터 시작하기때문에
    // 4번째 문자열을 비교하려면 index + 1 후 비교해야함
    // ex) 4번째 문자의 idx 는 3이니까
    return [...cipher].filter((str, idx) => (idx + 1) % code === 0).join('')
}