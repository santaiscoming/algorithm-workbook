import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]


def solution():
    max_삼각수 = next(i for i in range(10000) if (i * (i + 1)) / 2 >= 1000)
    삼각수 = [int((j * (j + 1)) / 2) for j in range(1, max_삼각수 + 1)]

    def dfs(depth, s, isPossible):
        if isPossible[0]:
            return

        if depth == 3:
            if s == 0:
                isPossible[0] = True
            return

        for i in 삼각수:
            dfs(depth + 1, s - i, isPossible)

    for num in nums:
        isPossible = [False]
        dfs(0, num, isPossible)
        if isPossible[0]:
            print(1)
        else:
            print(0)


solution()
