function solution(a, b) {
    const months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    const days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    const day = months.slice(0, a - 1).reduce((acc, cur) => acc + cur, 0) + b - 1
    
    console.log(day)
    return days[day % days.length]
}