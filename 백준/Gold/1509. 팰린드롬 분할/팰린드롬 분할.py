import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

str = input().rstrip()


def solve():
    n = len(str)
    isPal = [[False] * n for _ in range(n)]

    for length in range(n):
        for start in range(0, n - length):
            l = start
            r = start + length

            if l == r:
                isPal[l][r] = True
                continue

            if str[l] == str[r] and l + 1 == r:
                isPal[l][r] = True
                continue

            if str[l] == str[r] and isPal[l + 1][r - 1] == True:
                isPal[l][r] = True

    dp = [math.inf] * n

    for i in range(n):
        if isPal[0][i]:
            dp[i] = 1
        else:
            for j in range(1, i + 1):
                if isPal[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    print(dp[-1])


solve()
