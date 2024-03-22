import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())


def facto(n):
    if n == 0:
        return 1

    return facto(n - 1) * n


print(facto(N))
