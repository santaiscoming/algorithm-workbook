import sys


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

A, B, C = map(int, input().split())


def solution(A, B, C):
    memo = {}

    def power(a, b, c):
        if b == 0:
            return 1
        if b in memo:
            return memo[b]

        half = power(a, b // 2, c)
        if is_odd(b):
            half = half * half * a
        else:
            half = half * half

        memo[b] = half % c

        return memo[b]

    def is_odd(num):
        return num % 2 == 1

    print(power(A, B, C))


solution(A, B, C)
