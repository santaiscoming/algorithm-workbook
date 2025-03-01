import sys
import math
from collections import deque

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

R, C = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(R)]


def solution():
    min_time = math.inf
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    s = [(x, y) for x in range(C) for y in range(R) if mat[y][x] == "S"][0]
    d = [(x, y) for x in range(C) for y in range(R) if mat[y][x] == "D"][0]
    w = [(x, y) for x in range(C) for y in range(R) if mat[y][x] == "*"]
    visited = [[False] * C for _ in range(R)]

    waterQ = deque()
    [waterQ.append(pos) for pos in w]
    posQ = deque()
    posQ.append((s[0], s[1], 0))

    while posQ:
        for _ in range(len(waterQ)):
            x, y = waterQ.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                if (0 <= nx < C) and (0 <= ny < R) and mat[ny][nx] == ".":
                    mat[ny][nx] = "*"
                    waterQ.append((nx, ny))

        for _ in range(len(posQ)):
            x, y, time = posQ.popleft()

            if mat[y][x] == "D":
                min_time = min(min_time, time)
                break

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (
                    (0 <= nx < C)
                    and (0 <= ny < R)
                    and (mat[ny][nx] == "." or mat[ny][nx] == "D")
                    and not visited[ny][nx]
                ):
                    posQ.append((nx, ny, time + 1))
                    visited[ny][nx] = True

    print("KAKTUS" if min_time == math.inf else min_time)


solution()
