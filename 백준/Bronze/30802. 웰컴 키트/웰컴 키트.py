import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())


def solution():
    print(sum(shirt // t if shirt % t == 0 else shirt // t + 1 for shirt in shirts))
    print(n // p, n % p if n % p != 0 else 0)


solution()
