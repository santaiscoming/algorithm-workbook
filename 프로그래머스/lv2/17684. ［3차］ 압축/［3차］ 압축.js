function solution(msg) {   
    // 알파벳과 해당 색인 번호를 객체로 만듬
    const indexBook = Array.from({length : 26}, (_, idx) => idx + 65)
                           .reduce((map, curr) => {
                               map[String.fromCharCode(curr)] = curr - 64;        
                               return map;
                           }, {})
    let lastIdx = 27
    const result = []
    let nextWord = ''
    
    const strIterate = msg.split("").reduce((acc, cur) => {
        nextWord = acc + cur;
        if (indexBook[nextWord] === undefined) {
             indexBook[nextWord] = lastIdx++;
        } else {
             return acc + cur;
        }
      // K, A 같은것이 없으면 출력해라
        if (indexBook[acc] !== undefined) result.push(indexBook[acc]);
        return cur;
   }, '');
    
    result.push(indexBook[strIterate]);
    
    return result
}

// function solution(msg) {   
//     // 알파벳과 해당 색인 번호를 객체로 만듬
//     const indexBook = Array.from({length : 26}, (_, idx) => idx + 65)
//                            .reduce((map, curr) => {
//                                map[String.fromCharCode(curr)] = curr - 64;        
//                                return map;
//                            }, {})
//     let lastIdx = 27
//     const result = []
//     for (let char of msg) {
//         let currentStr = char
//         let nextStr = ''
//         for(let i = msg.indexOf(char); i < msg.length; i++) { 
//             // KA를 확인한다 (다음 단어까지 합친 문자)
//             nextStr += msg[i]
//                 // 없으면 K (처음단어)를 출력 result.push
//             if(!indexBook[nextStr] && indexBook[currentStr]) {
//                 // result.push(indexBook[currentStr])
//                 indexBook[nextStr] = lastIdx++
//                 continue;
//             }
//             result.push(indexBook[nextStr])
//             break;
//         }
//     }
    
//     return result
// }

// function solution(msg) {
//   const answer = [];
//   const indexBook = Array.from({length : 26}, (_, idx) => idx + 65)
//                      .reduce((map, curr) => {
//                          map[String.fromCharCode(curr)] = curr - 64;        
//                          return map;
//                      }, {});
//   let lastIdx = Object.keys(indexBook).length + 1  

//   let accStr = '';
//   for (const currentChar of msg) {
//     if (indexBook[accStr + currentChar] !== undefined) {
//       accStr += currentChar;
//     } else {
//       if (accStr !== '') {
//         answer.push(indexBook[accStr]);
//       }
//       indexBook[accStr + currentChar] = lastIdx++;
//       accStr = currentChar;
//     }
//   }
//   answer.push(indexBook[accStr]);
//   return answer;
// }
