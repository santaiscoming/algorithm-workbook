import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())


def solution():
    def dfs(nums, start):
        if len(nums) == m:
            print(*nums)
            return

        for i in range(start, n + 1):
            dfs([*nums, i], i)

    dfs([], 1)


solution()
