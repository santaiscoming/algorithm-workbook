import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a, b = map(int, input().split())


def solution():
    def gcd(a, b):
        while b:
            a, b = b, a % b

        return a

    print(gcd(a, b))
    print(a * b // gcd(a, b))



solution()
