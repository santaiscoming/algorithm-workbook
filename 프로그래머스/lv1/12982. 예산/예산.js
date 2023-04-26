function solution(d, budget) {
    d.sort((a, b) => a - b)
    let count = 0;
    
    for (let money of d) {
        if(budget < money) return count;
        budget -= money;
        count += 1;
    }
    console.log(budget)
    return count
}