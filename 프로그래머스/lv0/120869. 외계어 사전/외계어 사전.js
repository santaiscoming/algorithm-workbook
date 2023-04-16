function solution(spell, dic) {
   return dic.some((str) => [...str].sort().join('') === spell.sort().join('')) ? 1 : 2
}
