import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]


def solution():
    dp = [[-1] * i for i in range(1, n + 1)]
    dp[0][0] = tree[0][0]

    def recur(depth, idx):
        if depth >= n or idx > depth:
            return 0

        if dp[depth][idx] != -1:
            return dp[depth][idx]

        dp[depth][idx] = max(
            recur(depth + 1, idx) + tree[depth][idx],
            recur(depth + 1, idx + 1) + tree[depth][idx],
        )

        return dp[depth][idx]

    print(tree[0][0] + max(recur(1, 0), recur(1, 1)))


solution()
