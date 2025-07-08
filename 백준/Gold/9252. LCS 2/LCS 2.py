import sys

# sys.stdin = open("input.txt", "r")  # ❌
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()


def solve():
    n, m = len(s1), len(s2)
    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    def lcs(i, j):
        if i == 0 or j == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = lcs(i - 1, j - 1) + 1
        else:
            dp[i][j] = max(lcs(i - 1, j), lcs(i, j - 1))

        return dp[i][j]

    def buildLcs(i, j):
        if i == 0 or j == 0:
            return ""

        if s1[i - 1] == s2[j - 1]:
            return buildLcs(i - 1, j - 1) + s1[i - 1]
        elif dp[i - 1][j] > dp[i][j - 1]:
            return buildLcs(i - 1, j)
        else:
            return buildLcs(i, j - 1)

    lcsLength = lcs(n, m)
    print(lcsLength)
    if lcsLength > 0:
        print(buildLcs(n, m))


solve()
