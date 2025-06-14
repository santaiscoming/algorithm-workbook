import sys
from collections import Counter

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution3():
    counter = Counter(nums)
    uniqueNums = sorted(counter.keys())

    def dfs(picked):
        if len(picked) == m:
            print(*picked)
            return

        for num in uniqueNums:
            if counter[num] > 0:
                counter[num] -= 1
                dfs([*picked, num])
                counter[num] += 1

    dfs([])


solution3()


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


# solution()
