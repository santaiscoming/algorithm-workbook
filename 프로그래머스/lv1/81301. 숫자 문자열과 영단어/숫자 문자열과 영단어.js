function solution(s) {
    const numMap = {
      0: 'zero',
      1: 'one',
      2: 'two',
      3: 'three',
      4: 'four',
      5: 'five',
      6: 'six',
      7: 'seven',
      8: 'eight',
      9: 'nine',
    };

    Array.from({ length: 10 }, (_, idx) => {
      const regex = new RegExp(`${Object.values(numMap)[idx]}`, 'g');
      s = s.replace(regex, Object.keys(numMap)[idx]);
    });

    return parseInt(s);
}
