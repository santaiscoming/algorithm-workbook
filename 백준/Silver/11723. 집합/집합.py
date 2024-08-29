import sys
from typing import Set, List

# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

M = int(input())


def add(bit, x):
    return bit | (1 << x)


def remove(bit, x):
    return bit & ~(1 << x)


def check(bit, x):
    isExistBit = bit & (1 << x)

    if isExistBit:
        print(1)
    else:
        print(0)


def toggle(bit, x):
    return bit ^ (1 << x)


def all():
    return (1 << 21) - 1


def empty():
    return 0


def solution():
    bit = 1
    funcs = {
        "add": add,
        "remove": remove,
        "check": check,
        "toggle": toggle,
        "all": all,
        "empty": empty,
    }

    for _ in range(M):
        operator = input().split()
        cmd, num = operator if len(operator) == 2 else (operator[0], 0)
        num = int(num)

        if cmd != "empty" and cmd != "all":
            if cmd == "check":
                funcs[cmd](bit, num)
                continue

            bit = funcs[cmd](bit, num)

        else:
            bit = funcs[cmd]()


solution()
