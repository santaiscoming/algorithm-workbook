import sys
import math


# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


def solution():
    memo = [0] + [math.inf] * k

    for i in range(1, k + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], memo[i - coin] + 1)

    print(-1) if memo[k] == math.inf else print(memo[k])

    pass


solution()
