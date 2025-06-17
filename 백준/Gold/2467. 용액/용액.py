import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


def solution():
    l = 0
    r = n - 1
    prev = math.inf
    prevLv = 0
    prevRv = 0

    while l < r:
        lv = nums[l]
        rv = nums[r]
        acc = lv + rv

        if acc == 0:
            print(lv, rv)
            return

        if abs(acc) < abs(prev):
            prev = acc
            prevLv = lv
            prevRv = rv

        if acc > 0:
            r -= 1
        else:
            l += 1

    print(*sorted([prevLv, prevRv]))


solution()
