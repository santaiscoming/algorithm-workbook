function solution(x) {
    let hashad = [...String(x)].reduce((acc, cur) => acc + Number(cur), 0)
    
    return x % hashad === 0 ? true : false
}