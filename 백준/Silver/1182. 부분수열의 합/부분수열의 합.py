import sys
from typing import List
from itertools import combinations

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, S = [int(x) for x in input().split()]
nums = list(map(int, input().split()))


def solution():
    cnt = 0

    for i in range(1, N + 1):
        for comb in combinations(nums, i):
            if sum(comb) == S:
                cnt += 1

    print(cnt)


solution()
