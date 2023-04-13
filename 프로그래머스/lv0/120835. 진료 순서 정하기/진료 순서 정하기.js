function solution(emergency) {
    // emergency의 요소의 위치 idx를 기억해주자 (2차원배열)
    const emergencyMap = emergency.map((num, idx) => [num, idx + 1])
    
    // emergency 의 각 요소의 0번째 (위험도) 기준으로 정렬해주자
    emergencyMap.sort((a, b) => b[0] - a[0])
    
    //emergency 를 순회하면서 각 요소에 대해 emergencyMap의 0번째와 같을때 i + 1 을 리턴해주자
    return emergency.map((num, idx) => {
        for(let i = 0; i < emergencyMap.length; i++) {
            if(emergencyMap[i][0] === num) return i + 1
        }
    })

}