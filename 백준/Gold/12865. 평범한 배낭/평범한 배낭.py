import sys
import math

# sys.stdin = open("./input.txt", "r")  # 제출 전 제거
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]


# i 값이 0에서 시작하는것과 n-1 부터 시작하는것의 차이가 무엇을 의미하는지 생각하기
def topDown():
    memo = [[-1] * (k + 1) for _ in range(n)]
    s = [size for size, _ in items]
    p = [weight for _, weight in items]

    def dfs(i, size):
        if i < 0:
            return 0

        if memo[i][size] != -1:
            return memo[i][size]

        if size - s[i] >= 0:
            memo[i][size] = max(dfs(i - 1, size - s[i]) + p[i], dfs(i - 1, size))

        memo[i][size] = max(memo[i][size], dfs(i - 1, size))

        return memo[i][size]

    dfs(n - 1, k)
    print(memo[-1][-1])


# topDown()


def bottomUp():
    memo = [[0] * (k + 1) for _ in range(n + 1)]
    profits = [profit for _, profit in items]
    weights = [weight for weight, _ in items]

    for i in range(1, n + 1):
        for j in range(k, -1, -1):
            if j - weights[i - 1] >= 0:
                memo[i][j] = max(
                    memo[i - 1][j - weights[i - 1]] + profits[i - 1], memo[i - 1][j]
                )
            else:
                memo[i][j] = max(memo[i - 1][j], 0)

    # 순방향 순회시 2번 사용되는 문제 발생 가능성
    # for i in range(n):
    #     for j in range(k + 1):
    #         if j - weights[i] >= 0:
    #             memo[i][j] = max(
    #                 memo[i - 1][j - weights[i]] + profits[i], memo[i - 1][j]
    #             )
    #         else:
    #             memo[i][j] = max(memo[i - 1][j], 0)

    print(memo[-1][-1])


bottomUp()


def zeroToLenSolution():
    memo = [[-1] * (k + 1) for _ in range(n)]
    s = [size for size, _ in items]
    p = [weight for _, weight in items]

    def dfs(i, size):
        if i >= n:
            return 0

        if memo[i][size] != -1:
            return memo[i][size]

        if size - s[i] >= 0:
            memo[i][size] = max(dfs(i + 1, size - s[i]) + p[i], dfs(i + 1, size))

        memo[i][size] = max(memo[i][size], dfs(i + 1, size))

        return memo[i][size]

    print(dfs(0, k))


def fractionalSolution():
    items.sort(key=lambda x: (x[1] / x[0]), reverse=True)
    mp = 0

    def fractional(i, size):
        result = 0
        for j in range(i, n):
            w, p = items[j]

            if size >= w:
                result += p
                size -= w
            else:
                result += (p / w) * size
                break

        return result

    def knapsack(i, size, acc):
        nonlocal mp

        if acc + fractional(i, size) < mp:
            return

        if i >= n or size <= 0:
            mp = max(mp, acc)
            return

        w, p = items[i]

        if size >= w:
            knapsack(i + 1, size - w, acc + p)

        knapsack(i + 1, size, acc)

    knapsack(0, k, 0)

    print(mp)


# fractionalSolution()
