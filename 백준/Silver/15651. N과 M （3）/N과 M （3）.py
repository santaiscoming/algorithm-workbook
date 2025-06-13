import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())


def solution2():
    stack = [[]]

    while stack:
        nums = stack.pop()

        if len(nums) == m:
            print(*nums)
            continue

        for i in range(n, 0, -1):
            next = nums + [i]
            stack.append(next)


solution2()


def solution():
    def dfs(nums, depth):
        if depth == m:
            print(*nums)
            return

        for i in range(1, n + 1):
            dfs(nums + [i], depth + 1)

    dfs([], 0)


# solution()
