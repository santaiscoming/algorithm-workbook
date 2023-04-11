function solution(box, n) {
    return box.map((axis) => Math.floor(axis / n))
              .reduce((acc, cur) => acc * cur, 1);
}