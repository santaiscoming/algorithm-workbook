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

    w_q = deque()
    [w_q.append(pos) for pos in w]
    c_q = deque()
    c_q.append((s[0], s[1], 0))

    while True:
        if not c_q:
            break

        wl = len(w_q)
        wLoopCnt = 0
        while w_q:
            if wl == wLoopCnt:
                break

            x, y = w_q.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < C and 0 <= ny < R and mat[ny][nx] == ".":
                    mat[ny][nx] = "*"
                    w_q.append((nx, ny))

            wLoopCnt += 1

        cl = len(c_q)
        cLoopCnt = 0
        while c_q:
            if cl == cLoopCnt:
                break

            x, y, t = c_q.popleft()

            if (x, y) == d:
                min_time = min(t, min_time)
                continue

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < C
                    and 0 <= ny < R
                    and mat[ny][nx] != "*"
                    and mat[ny][nx] != "X"
                    and not visited[ny][nx]
                ):
                    c_q.append((nx, ny, t + 1))
                    visited[ny][nx] = True

            cLoopCnt += 1

    print("KAKTUS" if min_time == math.inf else min_time)


solution()
