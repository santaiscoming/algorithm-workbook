import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
stringSet = [input().strip() for _ in range(n)]
searchStrings = [input().strip() for _ in range(m)]


def solution():
    print(sum(1 for s in searchStrings if s in set(stringSet)))


solution()
