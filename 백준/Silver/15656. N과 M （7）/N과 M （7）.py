import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution2():
    nums.sort(reverse=True)

    stack = [[]]

    while stack:
        curr = stack.pop()

        if len(curr) == m:
            print(*curr)
            continue

        for num in nums:
            stack.append([*curr, num])


solution2()


def solution():
    nums.sort()

    def dfs(picked):
        if len(picked) == m:
            print(*picked)
            return

        for i in range(n):
            dfs([*picked, nums[i]])

    dfs([])


# solution()
