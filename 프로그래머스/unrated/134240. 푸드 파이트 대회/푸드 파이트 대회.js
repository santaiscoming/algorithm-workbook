function solution(food) {
    return food.reverse()
               .reduce((acc, cur, idx) => {
        const calorie = (food.length - idx - 1) + '';
        
        const foods = calorie.repeat(parseInt(cur / 2));
        console.log(typeof foods)
        
        return (foods) + acc + (foods);
    }, '0');
}