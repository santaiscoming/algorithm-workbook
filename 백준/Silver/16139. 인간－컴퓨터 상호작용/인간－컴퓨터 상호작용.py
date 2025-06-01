import sys
from collections import defaultdict

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
        result = 0

        for pos in counter[c]:
            if start <= pos <= end:
                result += 1

        print(result)


solution()
