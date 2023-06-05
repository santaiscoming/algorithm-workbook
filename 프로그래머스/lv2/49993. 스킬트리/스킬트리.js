function solution(skill, skill_trees) {
    let result = []
    
    const isCorrectTreeArr = skill_trees.map((tree, idx) => {
        const skillIdxArr = []
        const copySkill = [...skill];
        
        for(char of [...tree]) { 
            if(copySkill.length === 0) return true;
            
            // CBD에 해당 문자가 존재하면서 0번째 인지 확인 (즉, 순회하는 문자가 가장 처음 배워야하는 스킬인지 확인)
            if(copySkill.includes(char) && copySkill.indexOf(char) !== 0) return false;
            
            if(char === copySkill[0]) copySkill.shift();
        }
        
        return true;
    })
    
   return isCorrectTreeArr.filter((bool) => bool).length
}