import sys
from bisect import bisect_left

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


def solve():
    LIS = []

    for num in nums:
        if not LIS or num > LIS[-1]:
            LIS.append(num)
        else:
            idx = bisect_left(LIS, num)
            LIS[idx] = num

    print(len(LIS))


solve()
