function solution(players, callings) {
    let playerMap = players.reduce((map, curr, idx) => {
        map[curr] = idx + 1
        return map
    }, {})
    
    callings.forEach((passPlayer, idx) => {
        let findRank;
        findRank = playerMap[passPlayer]
        let nextPlayer = players[findRank - 2]
        players[findRank - 2] = passPlayer
        players[findRank - 1] = nextPlayer
        
        playerMap[passPlayer] -= 1;
        playerMap[nextPlayer] += 1;
    })
    // callings.forEach((passPlayer, idx) => {
    //     let findRank;
    //     findRank = playerMap[passPlayer]
    //     let nextPlayer = players[findRank - 2]
    //     playerMap[passPlayer] -= 1;
    //     playerMap[nextPlayer] += 1;
    //     players = Object.keys(Object.fromEntries(Object.entries(playerMap).sort((a, b) => a[1] - b[1])))
    // })
    
    return players
}