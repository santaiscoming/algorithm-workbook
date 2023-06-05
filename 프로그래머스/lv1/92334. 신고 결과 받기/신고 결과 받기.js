function solution(id_list, report, k) {
    // 첫 작성 수도코드
    // k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
    // return : id_list 기준으로 각 신고한 사람이 정지된 만큼의 숫자
    
    // 신고받은 횟수 (한 사람의 중복신고는 1회처리)
    const reportedCountList = {}
    // 각 유저마다 신고한 사람 info
    const reportMap = report.reduce((map, reportInfo) => {
    const [user, reportUser] = reportInfo.split(' ')
    if(!map[user]) {
        map[user] = [reportUser]
        return map
    }
    if(map[user].includes(reportUser)) return map
    map[user] = [...map[user], reportUser]
    return map
}, {})
    
    Object.values(reportMap).forEach((reportList) => {
        reportList.forEach((user) => {
            reportedCountList[user] = (reportedCountList[user] || 0) + 1
        })
    })
    
    // 정지 당한 사람 배열
    const bannedUsers = [];
    
    Object.entries(reportedCountList).forEach((reportedInfo) => {
        let [user, reportedCount] = reportedInfo
        reportedCount >= k ? bannedUsers.push(user) : ''
    })
    
    console.log({bannedUsers})
    
    // id_list를 돌면서 k 이상 신고당한 사람의 이름이 내가 신고한 사람들에 포함되어있으면 count ++;
    // because : 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution을 완성하세요
    return id_list.map(user => {
        let bannedsuccessCount = 0;
        if(!reportMap[user]) return 0
        reportMap[user].forEach(reportedUser => {
            if(bannedUsers.includes(reportedUser)) bannedsuccessCount++;
        })
        
        return bannedsuccessCount
    })
}
