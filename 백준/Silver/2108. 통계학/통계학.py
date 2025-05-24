import sys
import math
from collections import Counter

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]


def solution():
    매우작은수 = 1 / math.inf
    nums.sort()

    print(round(sum(nums) / n + 매우작은수))
    print(nums[n // 2])
    if len(Counter(nums)) > 1:
        print(
            Counter(nums).most_common(2)[1][0]
            if Counter(nums).most_common(2)[0][1] == Counter(nums).most_common(2)[1][1]
            else Counter(nums).most_common(1)[0][0]
        )
    else:
        print(Counter(nums).most_common(1)[0][0])
    print(nums[-1] - nums[0])


solution()
