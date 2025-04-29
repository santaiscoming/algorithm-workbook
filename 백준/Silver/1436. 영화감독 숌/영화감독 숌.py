import sys


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


def solution():
    m = 1
    num = 0

    while m <= n:
        num += 1
        if "666" in str(num):
            m += 1

    print(num)


solution()
