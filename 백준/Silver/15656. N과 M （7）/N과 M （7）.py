import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    nums.sort()

    def dfs(picked):
        if len(picked) == m:
            print(*picked)
            return

        for i in range(n):
            dfs([*picked, nums[i]])

    dfs([])


solution()
