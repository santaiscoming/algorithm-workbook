function solution(rsp) {
    return [...rsp].map((rsp) => {
        if(rsp == 2) return 0;
        if(rsp == 0) return 5;
        if(rsp == 5) return 2;
    }).join('')
}