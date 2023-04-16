function solution(sides) {
    let result = 0;
    // max = 배열에서 가장 큰값
    const max = Math.max(...sides)
    const min = Math.min(...sides)
    let restSide = 1;
    
    // 1. 배열의 max값이 가장 긴변인 경우 (나머지 변 < max && 나머지변 + 작은값 > max)
    while(restSide <= max) {
        if(restSide + min <= max) {
            restSide += 1;
            continue;
        }
        if(restSide + min > max) {
            result += 1;
            restSide += 1;
        }
    }
    
    // 2. 나머지 변이 가장 긴 변인 경우 (max < 나머지 변< 배열의 합 - 1)
    restSide = max;
    
    while(restSide < max + min - 1) {
        restSide += 1;
        result += 1;
    }
    
    return result;
}