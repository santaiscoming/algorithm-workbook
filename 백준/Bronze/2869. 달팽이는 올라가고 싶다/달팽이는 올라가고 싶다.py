import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a, b, v = map(int, input().split())


def solution():
    diff = a - b
    rest = v - a
    days = rest // diff

    if rest % diff > 0:
        days += 1

    print(days + 1)


solution()
