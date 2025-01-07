import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())


def solution(n: int):
    memo = {}

    def fibo(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if memo.get(n):
            return memo.get(n)
        else:
            memo[n] = fibo(n - 1) + fibo(n - 2)
            return memo[n]

    print(fibo(n))


solution(n)
