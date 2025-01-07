import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())


def solution(n: int):
    memo = {0: 0, 1: 1}

    def fibo(n):
        if n in memo:
            return memo.get(n)
        else:
            memo[n] = fibo(n - 1) + fibo(n - 2)
            return memo[n]

    print(fibo(n))


solution(n)
