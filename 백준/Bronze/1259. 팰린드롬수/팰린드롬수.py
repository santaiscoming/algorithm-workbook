import sys
from typing import Literal

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


cases = [list(map(int, n)) for n in iter(lambda: input().rstrip(), "0")]


def solution():
    def isPal(s) -> Literal["yes", "no"]:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return "no"

            left += 1
            right -= 1

        return "yes"

    for s in cases:
        print(isPal(s))


solution()
