import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]


def solution():
    # dp[i][j] = dp[i - 1]에서 1을 사용하지 않는 경우
    #            dp[i - 2]에서 2을 사용하지 않는 경우
    #            dp[i - 3]에서 3을 사용하지 않는 경우
    DIVISOR = 1_000_000_009
    dp = [[0] * 4 for _ in range(100001)]
    dp[1][1] = 1
    dp[1][2] = 0
    dp[1][3] = 0
    dp[2][1] = 0
    dp[2][2] = 1
    dp[2][3] = 0
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

    for i in range(4, 100001):
        dp[i][1] = dp[i - 1][2] + dp[i - 1][3] % DIVISOR
        dp[i][2] = dp[i - 2][1] + dp[i - 2][3] % DIVISOR
        dp[i][3] = dp[i - 3][1] + dp[i - 3][2] % DIVISOR

    for num in nums:
        print(sum(dp[num]) % DIVISOR)


solution()
