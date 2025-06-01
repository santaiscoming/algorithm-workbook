import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
qs = [((query := input().split())[0], int(query[1]), int(query[2])) for _ in range(q)]


def solution():
    counter = defaultdict(list)
    for i, c in enumerate(s):
        counter[c].append(i)

    for c, start, end in qs:
        left, right = bisect_left(counter[c], start), bisect_right(counter[c], end)

        print(right - left)


solution()
