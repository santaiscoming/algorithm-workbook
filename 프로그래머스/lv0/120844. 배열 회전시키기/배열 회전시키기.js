function solution(numbers, direction) {
    if(direction === 'right') return [...numbers.splice(numbers.length - 1, 1), ...numbers]
    
    if(direction === 'left') return [...numbers.slice(1), numbers[0]]
}