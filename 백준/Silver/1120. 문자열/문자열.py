import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

a, b = input().split()


def solution():
    result = math.inf

    for i in range(0, len(b) - len(a) + 1):
        diff_cnt = 0
        for ai in range(len(a)):
            bi = ai + i
            if a[ai] != b[bi]:
                diff_cnt += 1

        result = min(result, diff_cnt)

    print(result)


solution()
