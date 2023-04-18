function solution(A, B) {
    let count = 0;
    let arrA = [...A]
    let arrB = [...B]
    
    while(true) {
        if(count === arrA.length) return -1
        if(arrA.join('') === arrB.join('')) return count
        count += 1;
        arrA = [arrA.pop(), ...arrA]
    }
}