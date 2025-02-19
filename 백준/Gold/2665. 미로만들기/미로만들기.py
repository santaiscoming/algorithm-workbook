import sys
from collections import deque
import heapq
import math
from typing import Tuple, TypeAlias

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
global black, white
black = 0
white = 1

Tx: TypeAlias = int
Ty: TypeAlias = int


def dijkstra_solution(sx: int, sy: int) -> None:
    cost = [[math.inf] * n for _ in range(n)]
    cost[sy][sx] = 0

    q: Tuple[int, Tuple[Tx, Ty]] = []
    heapq.heappush(q, (cost[sy][sx], (sx, sy)))

    while q:
        prev_cost, (x, y) = heapq.heappop(q)

        for dy, dx in dir:
            ny, nx = dy + y, dx + x
            if (0 <= nx < n) and (0 <= ny < n):
                additional_cost = 1 if mat[ny][nx] == black else 0

                if cost[ny][nx] > prev_cost + additional_cost:
                    cost[ny][nx] = prev_cost + additional_cost
                    heapq.heappush(q, (cost[ny][nx], (nx, ny)))

    print(cost[-1][-1])


dijkstra_solution(0, 0)


def bfs_solution(sx, sy):
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


# bfs_solution(0, 0)
