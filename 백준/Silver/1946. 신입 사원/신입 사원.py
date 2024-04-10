import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T = int(input())


def solution(N, people):
    cnt = 1
    people.sort(key=lambda x: (x[0], x[1]))
    _, minimum_meet_rank = people[0]

    # 1등을 기준으로 하기에 0번째는 무조건 낮을 수 밖에 없다
    # 그렇다는것은 1등의 1번째 성적보다 높아야 들어갈 수 있다
    # 1등의 1번째 성적보다 낮다는것은 결국 2등 이하고 1등의 두 성적보다 낮다는것이기에

    for i in range(1, N):
        cur_person = people[i]
        _, meet_rank = cur_person

        if meet_rank > minimum_meet_rank:
            continue
        else:
            # [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
            # 예를들어 (4,2) 에서 minimum_meet_rank를 업데이트 하는데
            # 뒤에 7,3의 경우 meet_rank가 있지않느냐
            # 사실 의미가 없다 앞에 else로 타고 들어온 사람보다 서류 조건이 뒤떨어지고
            # 그 사람보다 2번째 순위 또한 낮다면 못들어가기때문
            minimum_meet_rank = meet_rank
            cnt += 1

    print(cnt)


for _ in range(T):
    N = int(input())
    people = [list(map(int, input().split())) for _ in range(N)]
    solution(N, people)
