import sys
from collections import Counter

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution3():
    counter = Counter(nums)
    uniqueNums = sorted(counter.keys())

    def dfs(picked, start):
        if len(picked) == m:
            print(*picked)
            return

        for i in range(start, len(uniqueNums)):

            num = uniqueNums[i]
            if counter[num] > 0:
                counter[num] -= 1
                dfs([*picked, num], i)
                counter[num] += 1

    dfs([], 0)


solution3()