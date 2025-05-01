import sys


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [input().split() for _ in range(n)]


def solution():
    [print(*v) for v in sorted(arr, key=lambda x: int(x[0]))]


solution()
