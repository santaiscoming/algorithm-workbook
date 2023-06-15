function solution(s) {
    const result = [];
    const limitCount = Math.floor(s.length / 2)
    // 예외처리
    if (s.length == 1) return 1;
    
    for (var i = 1; i <= limitCount; i++) {
        var b = '';
        var cnt = 1;
        var currentStr = s.slice(0, i);

        for (var j = i; j < s.length + i; j += i) {
            let nextStr = s.slice(j, i+j);
            if (currentStr === nextStr) {
                cnt++;
            } else {
                if (cnt != 1) b = b + String(cnt) + currentStr;
                else b = b + currentStr;
                
                currentStr = nextStr;
                cnt = 1;
            }
        }
        result.push(b.length);
    }

    return Math.min(...result);
}