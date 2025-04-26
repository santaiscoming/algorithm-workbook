import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

l = int(input())
s = input().rstrip()


def solution():
    M = 1234567891
    r = 31

    print(sum((ord(c) - 96) * (31**i) % M for i, c in enumerate(s)) % M)


solution()
