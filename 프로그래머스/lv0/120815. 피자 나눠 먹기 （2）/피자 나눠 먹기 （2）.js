function solution(n) {
    let pizza = 1;
    let pizzapiece = 6
    let person = n
    while(pizzapiece % person !== 0) {
        pizza += 1;
        pizzapiece += 6;
    }
    
    return pizza;
}