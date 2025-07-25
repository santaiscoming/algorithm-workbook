import sys
from itertools import product


# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution3():
    nums.sort(reverse=True)

    stack = [[]]
    
    while stack:
        curr = stack.pop()

        if len(curr) == m:
            print(*curr)
            continue

        prev = -1
        for num in nums:
            if prev != num:
                prev = num
                stack.append([*curr, num])


solution3()


def solution2():
    nums.sort()

    def dfs(picked):
        if len(picked) == m:
            print(*picked)
            return

        prev = -1
        for i in range(n):
            if nums[i] != prev:
                prev = nums[i]
                dfs([*picked, nums[i]])

    dfs([])


# solution2()


def solution():

    [print(*combi) for combi in sorted(set(product(sorted(nums), repeat=m)))]


# solution()
