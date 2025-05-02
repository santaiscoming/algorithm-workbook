import sys
from collections import deque


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]


def solution():
    def fuck445lip(n):
        return int(n + 0.5)

    rate = fuck445lip(n * 0.15)
    avgs = sorted(arr)[rate : n - rate]
    avg = fuck445lip(sum(avgs) / len(avgs)) if len(avgs) > 0 else 0

    print(avg)


solution()
