import sys
from functools import reduce

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]


def solution(N, stairs):
    if N <= 2:
        print(reduce(lambda acc, cur: acc + cur, stairs))
        return

    stairs = [0] + stairs
    dp = [0] * (N + 1)
    dp[0] = stairs[0]
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    for i in range(3, N + 1):
        # dp[n]은 어디서 올 수 있을까
        # 1. dp[n - 1] 즉, 자신의 1번 전에서 왔을 수 있다.
        # 1-1. 자신 전에서 올라오려면 나의 2칸 이전(dp[n - 1 - 2])에서 왔어야한다
        #      ? -> 나의 한칸 이전에 왔다면 dp[i - 1]은 문제 조건에 의해 2번째 이전에서 왔어야함
        # 1-2. 그렇다면 dp[n - 1]이 구해졌으므로 자신의 계딴을 더해주자
        # 2. dp[n - 2] 에서 왔을 수 있다.
        # 2-1. dp[n - 2]에서 온 경우 현재 자신의 계단을 더해주면 된다.
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    print(dp[-1])


solution(N, stairs)
