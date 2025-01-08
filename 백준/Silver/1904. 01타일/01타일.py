import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


N = int(input())
MODDING = 15746


# def memo(n):
#     if n % MODDING == 1:
#         return 1
#     if n % MODDING == 2:
#         return 2

#     new_n = n % MODDING
#     memo = [0] * (new_n + 1)
#     memo[1] = 1
#     memo[2] = 2

#     for i in range(3, new_n + 1):
#         memo[i] = (memo[i - 2] + memo[i - 1]) % MODDING

#     return memo[new_n]


def tabul(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    prev, curr = 1, 2

    for _ in range(3, n + 1):
        prev, curr = curr, (prev + curr) % MODDING

    return curr


def solution(n):
    print(tabul(n))


solution(n=N)
