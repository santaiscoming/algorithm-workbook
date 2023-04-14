function solution(my_string) {
    const regExp = /[a-zA-Z]/g
    const numList = my_string.split(regExp)
    return numList.reduce((acc, cur) => acc + Number(cur), 0)
}