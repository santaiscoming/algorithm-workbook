// const countOnes = (binaryNum) => {
//   let count = 0;
//   for (let i = 0; i < binaryNum.length; i++) {
//     if (binaryNum[i] === '1') {
//       count++;
//     }
//   }
//   return count;
// }


// function solution(n) {
//   let compareNum = n + 1;
//   let defaultOnesCount = countOnes(n.toString(2));

//   while (true) {
//     let compareNumCount = countOnes(compareNum.toString(2));

//     if (defaultOnesCount === compareNumCount) {
//       return compareNum;
//     }

//     compareNum++;


//   }
// }



function solution(n) {
    let compareNum = n + 1
    let binaryNum = n.toString(2)
    
    let sameOneCount = [...String(binaryNum)].filter((num) => Number(num)).length

    while(true) {
        let compareBinaryNum = compareNum.toString(2)
        let compareNumCount = [...String(compareBinaryNum)].filter((num) => Number(num)).length
        
     
        if(sameOneCount === compareNumCount) return compareNum
           compareNum++;
        
    }
}
