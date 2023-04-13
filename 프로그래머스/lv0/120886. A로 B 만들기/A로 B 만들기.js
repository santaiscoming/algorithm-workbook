const isEqaulString = (str1, str2) => {
    if(str1.length !== str2.length) return false;
    
    const notEqualStr = [...str1].filter((char, idx) => char !== str2[idx])
    
    return notEqualStr.length ? false : true
}

function solution(before, after) {
    const sortBefore = [...after].sort().join('')
    const sortAfter = [...before].sort().join('')
    
    return isEqaulString(sortBefore, sortAfter) ? 1 : 0
}