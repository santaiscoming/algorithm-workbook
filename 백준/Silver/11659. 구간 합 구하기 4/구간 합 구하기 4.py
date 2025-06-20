import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]


def solution():
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + nums[i - 1]

    for start, end in queries:
        print(dp[end] - dp[start - 1])


solution()
