import sys
from collections import deque
import math

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
global black, white
black = 0
white = 1


def solution(sx, sy):
    cost = [[math.inf] * n for _ in range(n)]
    cost[sy][sx] = 0

    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for dy, dx in dir:
            ny, nx = dy + y, dx + x

            if (0 <= ny < n) and (0 <= nx < n):
                additional_cost = 1 if mat[ny][nx] == black else 0
                if cost[ny][nx] > cost[y][x] + additional_cost:
                    cost[ny][nx] = cost[y][x] + additional_cost
                    q.append((nx, ny))

    print(cost[-1][-1])


solution(0, 0)
