import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    nums.sort()

    def dfs(picked, start, visited):
        if len(picked) == m:
            print(*picked)
            return

        for i in range(start, n):
            dfs([*picked, nums[i]], i + 1, visited)

    dfs([], 0, [False] * n)


solution()
