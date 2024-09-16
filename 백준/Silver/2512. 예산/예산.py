import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
budget_arr = list(map(int, input().split()))
M = int(input())


def solution(N, budget_arr, M):

    left, right = (0, max(budget_arr))
    result = 0
    mid = 0

    while True:

        # end condition
        if left > right:
            break

        mid = (right + left) // 2
        total = 0

        for req_budget in budget_arr:
            if req_budget > mid:
                total += mid
            else:
                total += req_budget

        # 추정예산의 총합이 총 예산보다 크다면 지급 불가 즉, right를 줄여야한다
        if total > M:
            right = mid - 1
        else:
            left = mid + 1
            result = mid

    print(result)


solution(N, budget_arr, M)
