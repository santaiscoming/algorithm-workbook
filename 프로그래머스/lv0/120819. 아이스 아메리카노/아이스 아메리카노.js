function solution(money) {
    let drinkCount = 0
    while(money >= 5500) {
        money -= 5500;
        drinkCount += 1;
    }
    
    return [drinkCount, money]
}