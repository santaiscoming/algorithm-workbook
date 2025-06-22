import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))


def solution():
    NOT_FOUND = math.inf
    acc = [0] * (n + 1)
    newNums = [0, *nums]

    for i in range(1, n + 1):
        acc[i] = acc[i - 1] + newNums[i]

    result = NOT_FOUND
    left, right = 0, 1

    while True:
        if right >= len(acc):
            break

        curSum = acc[right] - acc[left]

        if curSum >= s:
            result = min(result, right - left)
            left += 1
        else:
            right += 1

    print(0) if result == NOT_FOUND else print(result)


solution()
