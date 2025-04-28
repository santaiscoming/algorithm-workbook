import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


def solution():
    arr = [0] * 10001

    for _ in range(n):
        arr[int(input())] += 1

    for i, v in enumerate(arr):

        while v > 0:
            v -= 1
            print(i)


solution()
