import sys
from functools import reduce

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

lines = sys.stdin.readlines()
semos = []
for line in lines:
    semos.append(list(map(int, line.split())))


def solution():
    for semo in semos:
        if reduce(lambda x, y: x + y, semo) == 0:
            continue

        long = max(semo)
        sum = reduce(lambda x, y: x + y, semo) - long
        x, y, z = semo
        if sum <= long:
            print("Invalid")
        elif x == y == z:
            print("Equilateral")
        elif x == y or y == z or z == x:
            print("Isosceles")
        else:
            print("Scalene")


solution()
