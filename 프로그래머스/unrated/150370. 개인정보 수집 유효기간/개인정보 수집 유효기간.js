function solution(today, terms, privacies) {

    const todayMap = today.split('.').reduce((map, curr, idx) => {
        if(idx === 0) {
            map['year'] = Number(curr)
            return map
        }
        if(idx === 1) {
            map['month'] = Number(curr)
            return map
        }
        map['day'] = Number(curr)
        return map
    }, {})
    
    const termsMap = terms.map((term) => term.split(' '))
                          .reduce((map, currTerm) => {
                              let [termType, month] = currTerm
                              map[termType] = Number(month)
                              return map
                          }, {})
    
    console.log(todayMap, termsMap)
    
    const result =  privacies.map(person => {
                        // '2021.05.02 A'
                let [period, type] = person.split(' ')
                let [year, month, day] = period.split('.').map(date => Number(date))
                let validPeriod = termsMap[type]
                month = month + validPeriod
                if(month > 12) {
                    while(true) {
                        if(month <= 12) break
                        year++;
                        month -= 12
                    }
                }
                console.log({person ,year, month, day})
                // 현재의 연도가 유효기간의 연도보다 크면 파기x
                if(year > todayMap['year']) return false
                // 현재 달이 파기해야할 달보다 크면 파기x
                if(month > todayMap['month'] && year >= todayMap['year']) return false
                // 연도가 크면 위위에서 걸리고 달이 크면 위에서 걸리고 그렇다면 month과 yaer이 같다는 전제하에 day가 크면 파기x
                if(day > todayMap['day'] && year === todayMap['year'] && month === todayMap['month']) return false

                return true
            })
    let realResult = [];
    console.log(result)
    
    result.forEach((bool, idx) =>  bool ? realResult.push(idx + 1) : '')

    return realResult
}