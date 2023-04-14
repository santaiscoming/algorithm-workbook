function solution(word) {
    const vowels = [...'AEIOU']
//     A       E           I       O       U           +1 -1
//   AA AE   EA    EI
// AAA      EAA EAI 
    const vowelsMap = {}
// 1. dfs를 vowels의 length만큼 반복해줘야해
//    1-1. dfs를 돌면서 문자열을 만들고 해당 문자열이 몇번째에 생성됐는지 기록해야해. -> 객체의 value로 idx++
//    1-2. basecode : 만든 문자열의 길이가 vowels.length 같아질때 return
//    1-3. str, idx 가 필요해
    let idx = 1;
    const dfs = (strSum) => {
        // 탈출조건
        if(strSum.length  === vowels.length + 1) return;
        
        // 수행동작
        vowelsMap[strSum] = idx++;
        
        vowels.forEach((vowel) => {
            dfs(strSum + vowel)
        })
    }
    
    dfs("")

    
    return vowelsMap[word] - 1
}