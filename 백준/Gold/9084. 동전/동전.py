import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

global T
global cases


T = int(input())
cases = [
    [int(input()), list(map(int, input().split())), int(input())] for _ in range(T)
]

# idx : price
# memo[idx] : 경우의 수

# ex)
# coins = [1, 2], price = 5
# memo[idx] = memo[idx - coin]
# 5원 를 만들기 위한 경우의 수 = 3원의 경우의 수 + 2원 1개사용


def solution():
    for case in cases:
        _, coins, price = case

        memo = [0] * (price + 1)
        memo[0] = 1
        for coin in coins:
            for i_p in range(coin, price + 1):
                memo[i_p] += memo[i_p - coin]

        print(memo[i_p])


solution()
