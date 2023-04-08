function solution(num_list) {
//     const even = num_list.filter((num) => num % 2 === 0);
//     const odd = num_list.filter((num) => num % 2 === 1);
    
//     return [even.length, odd.length]
    
    return num_list.reduce((acc, cur) => (cur & 1 ? acc[1]++ : acc[0]++, acc), [0, 0])
}