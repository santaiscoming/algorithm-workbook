import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

global M, N

M, N = map(int, input().split())


def is_sosu(num):
    if num == 1:
        return False

    return True and all(
        False if num % i == 0 else True for i in range(2, int(math.sqrt(num)) + 1)
    )


def solution():
    nums = [i for i in range(M, N + 1)]

    list(map(print, filter(is_sosu, nums)))


solution()
