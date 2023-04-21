function solution(s){
    const pFrequency =[...s.toLowerCase()].filter((str) => str === 'p').length;
    const yFrequency =[...s.toLowerCase()].filter((str) => str === 'y').length;
    
    return pFrequency === yFrequency ? true : false;
}