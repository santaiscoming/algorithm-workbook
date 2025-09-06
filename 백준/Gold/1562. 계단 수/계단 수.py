import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())


def solve():
    MOD = 10**9
    ALL_USED = (1 << 10) - 1
    dp = dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]

    for num in range(1, 10):
        dp[1][num][1 << num] = 1

    for i in range(2, n + 1):
        for num in range(10):
            row = dp[i - 1][num]

            for mask in range(1 << 10):
                cnt = row[mask]
                if cnt == 0:
                    continue
                if num > 0:
                    newMask = mask | (1 << (num - 1))
                    dp[i][num - 1][newMask] = (dp[i][num - 1][newMask] + cnt) % MOD
                if num < 9:
                    newMask = mask | (1 << (num + 1))
                    dp[i][num + 1][newMask] = (dp[i][num + 1][newMask] + cnt) % MOD

    result = 0
    for num in range(10):
        result = (result + dp[n][num][ALL_USED]) % MOD
    print(result)


solve()
