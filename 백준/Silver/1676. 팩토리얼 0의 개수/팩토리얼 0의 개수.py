import sys
from typing import List


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


def solution():
    def facto(n):
        if n <= 1:
            return 1

        return n * facto(n - 1)

    count = 0
    for v in str(facto(n))[::-1]:
        if v != "0":
            break

        count += 1

    print(count)


solution()
