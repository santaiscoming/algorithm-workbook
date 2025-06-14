import sys
from itertools import product

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    [print(*combi) for combi in sorted(set(product(sorted(nums), repeat=m)))]


solution()
