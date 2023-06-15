function solution(keymap, targets) {
    
    let result = [];
    let keyPressMap = new Map();
                                            // get, set, has(키를 갖고있느냐) 
    // key : 누르는 자판
    // value : 누르는 횟수 -> idx + 1
    keymap.forEach((val,i)=> {
        // console.log(`현재 실행된 콜백의 순서는 ${i + 1}번째, 현재 실행된 콜백의 value : ${val}`);
        
        // [B C E F D] 일떄
        // 현재 keyPressMap은 { 'A' => 3, 'B' => 2, 'C' => 4, 'D' => 5 }
        [...val].forEach((el,i)=>{
            // console.log(`안쪽 forEach에서 현재 value : ${el} 입니다`)
            // if : 이미 키가 있고, 내가 더 빠르면 나의 idx + 1을 keypressMap에 넣자
            // 현재 나는 B, 현재 나의 횟수 -> i + 1
            if(keyPressMap.has(el)) {
                // console.log(`나있음, 지금 들어있는 나는 ${keyPressMap.get(el)}`)
                    keyPressMap.set(el, Math.min(i + 1, keyPressMap.get(el)))
                    return
            }
             keyPressMap.set(el, i + 1)
                
        })
    // console.log(`야호! 드디어 ${i + 1} 번째 함수가 끝났어 ! 지금 foreach를 돌고난뒤 keyPressMap은`, keyPressMap) 
    })
    console.log(keyPressMap)
    
    targets.forEach((val, i) => {
        // curVal = "ABCD" next : AABB
        // keyPressMap => 우리가 왼쪽 오른쪽 키보드에서 등장횟수인데 가장 빠른애들만 담았어
        // ABCD 를 돌면서 A, B, C, D를 keyPressMap에서 가져와서 계속 더해주면 되겠다.
        // result.push(sum)
        let sum = 0;
        
        [...val].forEach((el, i) => {
            // target을 도는 el이 keyPressMap에 없다면 아무것도 하지마 === 해당 함수를 종료해버려 -> break -> forEach에서는  return
            if(!keyPressMap.has(el)) return
            sum += keyPressMap.get(el);
        })
        if(sum === 0) {
            result.push(-1)
            return
        }
        result.push(sum)
    })

    return result
}

// forEach의 실행원리
 //    ["ABACD", "BCEFD"]
 // keymap.forEach((v , i) => {~~~}
 //                (v,  i) => {~~~}
 //               )