import sys
import math


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr1 = map(int, input().split())
m = int(input())
arr2 = map(int, input().split())


def solution():
    nums = set(arr1)

    for v in arr2:
        print(1) if v in nums else print(0)


solution()
