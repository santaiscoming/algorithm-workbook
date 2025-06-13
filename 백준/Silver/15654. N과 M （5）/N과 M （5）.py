import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    nums.sort()

    def dfs(pickedNums, visited):
        if len(pickedNums) == m:
            print(*pickedNums)
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs([*pickedNums, nums[i]], visited)
                visited[i] = False

    dfs([], [False] * n)


solution()
