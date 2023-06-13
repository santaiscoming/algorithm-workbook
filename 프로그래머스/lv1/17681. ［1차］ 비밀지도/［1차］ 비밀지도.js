function solution(n, arr1, arr2) {
    const result = Array.from({length : n}, () => [...' '.repeat(n)])

    arr1 = arr1.map((num) => {
        let binary = num.toString(2)
        let diff = n - binary.length
        return [...'0'.repeat(diff), ...binary]
    })
    
    arr2 = arr2.map((num) => {
        let binary = num.toString(2)
        let diff = n - binary.length
        return [...'0'.repeat(diff), ...binary]
    })
    
    arr1.forEach((binaryArr, outerIdx) => {
        arr1.forEach((bin, innerIdx) => {
            if(arr1[outerIdx][innerIdx] === '1' || arr2[outerIdx][innerIdx] === '1') result[outerIdx][innerIdx] = '#'
        })
    })

    return result.map(arr => arr.join(''))
}