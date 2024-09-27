import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# n : 팀개수
# k : 문제 개수
# t : 우리팀 id
# m : 로그 엔트리 개수

T = int(input())
info = [
    [(n, k, t, m), [list(map(int, input().split())) for _ in range(m)]]
    for n, k, t, m in (map(int, input().split()) for _ in range(T))
]


def solution():
    results = []
    my_temas = []

    for test_info, logs in info:
        team_cnt, prob_cnt, my_team_id, logs_cnt = test_info

        my_temas.append(my_team_id)

        templete = {
            i: {"total": 0, "submit_cnt": 0, "last_submit": 0, "problems": {}}
            for i in range(1, team_cnt + 1)
        }

        for idx, (id, prob_num, score) in enumerate(logs):
            if prob_num not in templete[id]["problems"]:
                templete[id]["problems"][prob_num] = score
            else:
                templete[id]["problems"][prob_num] = max(
                    templete[id]["problems"][prob_num], score
                )

            templete[id]["total"] = sum(templete[id]["problems"].values())
            templete[id]["last_submit"] = idx
            templete[id]["submit_cnt"] += 1

        results.append(templete)

    for idx, result in enumerate(results):

        sorted_result = sorted(
            result.items(),
            key=lambda item: (
                -item[1]["total"],
                item[1]["submit_cnt"],
                item[1]["last_submit"],
            ),
        )

        for grade, team_info in enumerate(sorted_result):
            id, *_ = team_info
            if id == my_temas[idx]:
                print(grade + 1)


solution()
