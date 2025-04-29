import sys
from typing import List


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

arr: List[str] = [input().rstrip() for _ in range(3)]


def solution():
    def printFizzBuzz(n: int):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

    for i, v in enumerate(arr):
        if v.isdigit():
            num = int(v)
            rest = 3 - i
            printFizzBuzz(num + rest)
            return

    print(1)


solution()
