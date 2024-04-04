import sys
import heapq

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline


N = int(input())


# def fibo(n):
#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1

#     # f(n) = f(n-1) + f(n - 2)
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]

#     return dp[n]


dp = [0] * (N + 1)
dp[1] = 1


def fibo_recur(n):
    if n == 1 or n == 0:
        return dp[n]

    if dp[n] != 0 and n != 0:
        return dp[n]

    dp[n] = fibo_recur(n - 1) + fibo_recur(n - 2)

    return dp[n]


def solution(n):
    result = fibo_recur(n)

    print(result)


solution(N)
