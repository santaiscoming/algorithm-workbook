function solution(angle) {
    const positiveAngle = parseInt(angle)
    if(positiveAngle < 90) return 1
    if(positiveAngle === 90) return 2
    if(positiveAngle < 180) return 3
    if(positiveAngle === 180) return 4
}