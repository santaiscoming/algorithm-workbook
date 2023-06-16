function solution(s) {
    const result = [];
    const limitCount = Math.floor(s.length / 2)
    // 예외처리
    if (s.length == 1) return 1;
    
    for (let i = 1; i <= limitCount; i++) {
        let accStr = '';
        let count = 1;
        let sliceStr = s.slice(0, i);

        for (let j = i; j < s.length + i; j += i) {
            let nextSliceStr = s.slice(j, i+j);
            if (sliceStr === nextSliceStr) {
                count++;
            } else {
                if (count !== 1) accStr += String(count) + sliceStr;
                if (count === 1) accStr += sliceStr;
                
                sliceStr = nextSliceStr;
                count = 1;
            }
        }
        result.push(accStr.length);
    }

    return Math.min(...result);
}