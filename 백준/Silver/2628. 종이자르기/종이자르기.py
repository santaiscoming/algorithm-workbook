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

    grid = [[-1 for _ in range(len(col_cuts) - 1)] for _ in range(len(row_cuts) - 1)]

    max_area = 0
    piece_id = 0

    for r in range(len(row_cuts) - 1):
        for c in range(len(col_cuts) - 1):

            area = (row_cuts[r + 1] - row_cuts[r]) * (col_cuts[c + 1] - col_cuts[c])
            grid[r][c] = piece_id
            max_area = max(max_area, area)
            piece_id += 1

    return max_area


print(solution())
