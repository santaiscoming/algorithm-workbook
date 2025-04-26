import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

inputs = []
while True:
    l1, l2, l3 = map(int, input().split())

    if (l1, l2, l3) == (0, 0, 0):
        break

    inputs.append([l1, l2, l3])


def solution():
    for tri in inputs:
        tri.sort()
        s, m, l = tri

        if l**2 == s**2 + m**2:
            print("right")
        else:
            print("wrong")


solution()
