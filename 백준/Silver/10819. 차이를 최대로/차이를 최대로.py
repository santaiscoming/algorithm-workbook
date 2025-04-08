import sys


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n = int(input())
numss = list(map(int, input().split()))


def solution():
    maximum = 0
    visited = [False] * n

    def calc(nums):
        acc = 0

        for i in range(1, len(nums)):
            acc += abs(nums[i - 1] - nums[i])

        return acc

    def recur(nums):
        nonlocal maximum

        if len(nums) == n:
            cur_value = calc(nums)

            if cur_value > maximum:
                maximum = cur_value

            return

        for i, num in enumerate(numss):
            if not visited[i]:
                visited[i] = True
                recur([*nums, num])
                visited[i] = False

    for i, num in enumerate(numss):
        visited[i] = True
        recur([num])
        visited[i] = False

    print(maximum)


solution()
