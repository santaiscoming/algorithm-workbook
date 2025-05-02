import sys
from collections import Counter


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


def solution():
    counter = Counter(arr1)
    print(*[counter.get(v) if counter.get(v) is not None else 0 for v in arr2])


solution()
