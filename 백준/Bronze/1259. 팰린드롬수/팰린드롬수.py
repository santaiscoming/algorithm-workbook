import sys
from typing import Literal

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


cases = [list(map(int, n)) for n in iter(lambda: input().rstrip(), "0")]


def solution():
    def isPal(s) -> Literal["yes", "no"]:
        return "yes" if s == s[::-1] else "no"

    def isPal2(s) -> Literal["yes", "no"]:
        return "yes" if all(a == b for a, b in zip(s, s[::-1])) else "no"

    for s in cases:
        print(isPal2(s))


solution()
