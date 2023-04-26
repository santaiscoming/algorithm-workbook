function solution(s) {
    const words = s.split(' ');
    return words.map((word) => 
                     [...word].map((char, idx) => idx % 2 === 0 ? char.toUpperCase() : char.toLowerCase()))
                .map((wordArr) => wordArr.join('')).join(' ')
}