function solution(numlist, n) {
    return numlist.sort((num1, num2) => {
        const [diffNum1, diffNum2] = [Math.abs(num1 -n), Math.abs(num2 -n)]

        if(diffNum1 === diffNum2) return num2 - num1;

        return diffNum1 - diffNum2;
    })
}