import sys


# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    nums.sort()

    def dfs(picked, start):
        if len(picked) == m:
            print(*picked)
            return

        prev = -1
        for i in range(start, n):
            if nums[i] != prev:
                prev = nums[i]
                dfs([*picked, nums[i]], i)

    dfs([], 0)


solution()