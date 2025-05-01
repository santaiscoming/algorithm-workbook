import sys


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def solution():
    [print(*v) for v in sorted(arr, key=lambda x: (x[0], x[1]))]


solution()
