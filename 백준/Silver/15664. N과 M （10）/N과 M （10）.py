import sys
from collections import Counter
from itertools import combinations

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    [print(*combi) for combi in sorted(set(combinations(sorted(nums), m)))]


solution()