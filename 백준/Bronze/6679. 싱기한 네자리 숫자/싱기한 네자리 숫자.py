import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline


def solution():
    def digit_sum(num, base):
        total = 0
        while num > 0:
            rest = num % base
            total += rest
            num //= base

        return total

    for i in range(1000, 10000):
        if digit_sum(i, 10) == digit_sum(i, 12) == digit_sum(i, 16):
            print(i)


solution()
