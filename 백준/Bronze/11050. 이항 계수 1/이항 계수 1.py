import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())


def solution():
    def facto(n):
        result = 1

        for v in range(1, n + 1):
            result *= v

        return result

    print(int(facto(n) / (facto(k) * facto(n - k))))


solution()
