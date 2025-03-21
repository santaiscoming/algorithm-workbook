function solution(friends, gifts) {
    const nextMonth = friends.reduce((acc, cur) => {
        acc[cur] = 0
        return acc
    }, {})
    const giftRate = friends.reduce((acc, cur) => {
        acc[cur] = 0
        return acc
    }, {})
    const info = friends.reduce((acc, name) => {
        acc[name] = Object.fromEntries(
            friends.filter((f) => (f !== name)).map((f) => [f, 0]))
        return acc
        }, {})

    
    gifts.forEach((v) => {
        const [from, to] = v.split(' ')
        
        info[from][to] += 1
        giftRate[from] += 1
        giftRate[to] -= 1
    })
    const doneNames = []
    
    Object.entries(info).forEach(([from, giveInfo]) => {
        Object.entries(giveInfo).forEach(([to, cnt]) => {
            if (doneNames.includes(to)) {
                return
            }
            const 내가준거 = cnt
            const 쟤한테받은거 = info[to][from]
            if (내가준거 > 쟤한테받은거) {
                nextMonth[from] += 1
                return
            }
            
            if (내가준거 < 쟤한테받은거) {
                nextMonth[to] += 1
                return
            }
            
            if (giftRate[from] > giftRate[to]) {
                nextMonth[from] += 1
            } else if (giftRate[from] < giftRate[to]) {
                nextMonth[to] += 1
            }
        })
        doneNames.push(from)

    })

    return Math.max(...Object.entries(nextMonth).map(([k, v]) => v))
}