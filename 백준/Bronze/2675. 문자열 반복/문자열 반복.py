import sys
from functools import reduce

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T = int(input())
words = [input().strip().split(" ") for _ in range(T)]


for [repeatCount, word] in words:
    repeatCount = int(repeatCount)
    print(reduce(lambda prev, curr: prev + (curr) * repeatCount, word, ""))
