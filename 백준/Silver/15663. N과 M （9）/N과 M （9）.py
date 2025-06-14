import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    nums.sort()
    resultSet = set()

    def dfs(picked, visited):
        if len(picked) == m and tuple(picked) not in resultSet:
            print(*picked)
            resultSet.add(tuple(picked))
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs([*picked, nums[i]], visited)
                visited[i] = False

    dfs([], [False] * n)


solution()
