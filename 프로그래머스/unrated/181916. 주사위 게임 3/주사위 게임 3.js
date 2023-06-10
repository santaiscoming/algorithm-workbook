function solution(a, b, c, d) {
let diceRolls = new Map();
[a, b, c, d].forEach((roll) => {
diceRolls.set(roll, (diceRolls.get(roll) || 0) + 1);
});
let score = 0;
let keys = Array.from(diceRolls.keys());
let values = Array.from(diceRolls.values());
console.log(diceRolls)
if (values.includes(4)) {
score = 1111 * keys[values.indexOf(4)];
} else if (values.includes(3)) {
// Three dices have the same number and one is different
let p = keys[values.indexOf(3)];
let q = keys[values.indexOf(1)];
score = Math.pow(10 * p + q, 2);
} else if (values.includes(2)) {
// if 2개가 같은게 있다면
// values의 length가 2인가 ? -> two pair
// length가 2가 아니다 -> ex) 2 2 1 3 => values : 2 1 3
// Two pairs of dices have the same numbers
if(values.length === 2) {
let idx1 = values.indexOf(2);
let p = keys[idx1];
values[idx1] = -1; // Prevent selecting the same index
let idx2 = values.indexOf(2);
let q = keys[idx2];
score = (p + q) * Math.abs(p - q);
} else if (values.length !== 2) {
// Two dices have the same number and the other two dices have different numbers
let p = keys[values.indexOf(2)];
let idx1 = values.indexOf(1);
let q = keys[idx1];
values[idx1] = -1; // Prevent selecting the same index
let idx2 = values.indexOf(1);
let r = keys[idx2];
score = q * r;
}

} else if (values.includes(1)) {
// All four dices have different numbers
score = Math.min(...keys);
}

return score;
}