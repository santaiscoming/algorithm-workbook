// 의상의 종류가 몇개인지 찾아주자
// 조합이라고 하였다. 안경이 2개고 모자가 3개라면 조합할 수 있는 경우의수는 6가지 (2 * 3)
// 근데 안입는 경우가 있다 -> 각 조합 + 1
function solution(clothes) {
    var answer = 0;
    const clothesMap = new Map()
    
    // map을 그려주자
    for (let [cloth, type] of clothes) {
        // 안입는 경우가 있으니 경우의수 + 1 (초기 경우의 수를 1로 해주자)
        if(!clothesMap.has(type)) clothesMap.set(type, 1);
        clothesMap.set(type, clothesMap.get(type) + 1)
    }
    // yellow_hat, green_turban, 안입어
    // blue_sunglasses, 안입어
    return [...clothesMap.values()].reduce((acc, cur) => acc * cur, 1) - 1;
    // -1 해준 이유는 둘다 안입으면 안돼 (최대 1가지 의상 착용)
}