function solution(sides) {
   return sides.reduce((acc, cur) => acc + cur ) - Math.max(...sides) > Math.max(...sides) ? 1 : 2
}