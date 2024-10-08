import sys

# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

N = int(input())


def solution(N):
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 0
    dp[3] = 1

    for i in range(4, N + 1):
        if dp[i - 3] == 1 or dp[i - 1] == 1:
            dp[i] = 0
        else:
            dp[i] = 1

    if dp[N] == 1:
        print("SK")
    else:
        print("CY")


solution(N)
