import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]


def solution():
    longest = 0
    result = 0

    for i in range(n - 1, -1, -1):
        if arr[i] > longest:
            longest = arr[i]
            result += 1

    print(result)


solution()
