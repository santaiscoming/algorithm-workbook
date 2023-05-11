

function solution(ingredient) {
    let answer = 0;
    const bugger = [];

    for (let i = 0; i < ingredient.length; i++) {
        bugger.push(ingredient[i]);
        if (bugger.length >= 4) {
        if (bugger[bugger.length - 4] === 1 && bugger[bugger.length - 3] === 2 && bugger[bugger.length - 2] === 3 && bugger[bugger.length - 1] === 1) {
            Array.from({length: 4}, () => bugger.pop())

            answer += 1;
            }
        }
    }

    return answer;
}