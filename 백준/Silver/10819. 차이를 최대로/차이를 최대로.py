import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


def solution():
    def sum(arr):
        result = 0

        for i in range(1, len(arr)):
            result += abs(arr[i - 1] - arr[i])

        return result

    result = 0

    def dfs(arr, visited):
        nonlocal result

        if len(arr) == n:
            result = max(sum(arr), result)
        else:
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    dfs(arr + [nums[i]], visited)
                    visited[i] = False

    dfs([], [False] * n)
    print(result)


solution()
