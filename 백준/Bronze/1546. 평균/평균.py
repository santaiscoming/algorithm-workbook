import sys
from typing import Literal

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))


def solution():
    print(sum(score / max(scores) * 100 for score in scores) / n)


solution()
