import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]


def solve():
    dp = [[False] * n for _ in range(n)]

    for s in range(n):
        l = s
        r = s

        while l >= 0 and r < n and nums[l] == nums[r]:
            dp[l][r] = True
            l -= 1
            r += 1

        l = s
        r = s + 1

        while l >= 0 and r < n and nums[l] == nums[r]:
            dp[l][r] = True
            l -= 1
            r += 1

    for s, e in queries:
        print(int(dp[s - 1][e - 1]))


solve()
