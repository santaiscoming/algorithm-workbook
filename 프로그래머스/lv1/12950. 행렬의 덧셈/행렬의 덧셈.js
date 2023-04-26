function solution(arr1, arr2) {
     return arr1.map((e,idx) => arr2[idx].map((v,innerIdx) => arr1[idx][innerIdx]+arr2[idx][innerIdx]))
}