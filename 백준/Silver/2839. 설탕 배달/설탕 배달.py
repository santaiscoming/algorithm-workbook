import sys


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


def solution():
    result = -1

    for five in range(0, n + 1, 5):
        fiveCount = five // 5
        rest = n - five

        if rest % 3 == 0:
            result = fiveCount + rest // 3

    print(result)


solution()
