import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


w, h = map(int, input().split())
n = int(input())
cuts = [list(map(int, input().split())) for _ in range(n)]


def solution():
    row_cuts = [0, h]
    col_cuts = [0, w]

    for direction, pos in cuts:
        if direction == 0:
            row_cuts.append(pos)
        else:
            col_cuts.append(pos)

    row_cuts.sort()
    col_cuts.sort()

    max_area = 0

    for i in range(len(row_cuts) - 1):
        for j in range(len(col_cuts) - 1):
            top_left = (row_cuts[i], col_cuts[j])
            bottom_right = (row_cuts[i + 1], col_cuts[j + 1])

            lr, lc = top_left
            rr, rc = bottom_right

            max_area = max((rr - lr) * (rc - lc), max_area)

    print(max_area)


solution()
