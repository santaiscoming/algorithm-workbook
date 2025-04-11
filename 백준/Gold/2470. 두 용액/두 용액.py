import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def solution():
    arr.sort()

    result = []
    left, right = 0, n - 1
    prev = math.inf

    while left < right:
        mix = arr[left] + arr[right]

        if abs(mix) < abs(prev):
            prev = mix
            result = [arr[left], arr[right]]

        if mix > 0:
            right -= 1
        else:
            left += 1

    print(*result)


solution()
