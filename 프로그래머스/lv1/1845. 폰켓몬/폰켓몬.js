function solution(nums) {
    // 최대 가질 수 있는 포켓몬 수
    const maxMon = nums.length / 2;
    // 포켓몬의 종류
    const notDuplicatedMon = new Set(nums).size

    // 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return
    if(maxMon > notDuplicatedMon) return notDuplicatedMon
    return maxMon
}