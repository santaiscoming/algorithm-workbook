function solution(box, n) {
    return box.map((axis) => Math.floor(axis / n))
              .reduce((acc, cur) => acc * cur, 1);
    
    // let [x, y, z] = box
    // return Math.floor(x / n) * Math.floor(y / n) * Math.floor(z / n)
}