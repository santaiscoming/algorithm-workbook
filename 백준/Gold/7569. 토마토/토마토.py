import sys
from collections import deque

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[] for _ in range(H)]

for i in range(H):
    for j in range(N):
        row = list(map(int, input().split()))
        box[i].append(row)


def solution():
    # 위부터 시계방향, + 위아래 (x, y, z)
    directions = [[0, -1, 0], [1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]
    max_days = 0
    Q = deque()

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    Q.append((x, y, z, 0))

    if len(Q) == N * M * H:
        print(0)
        return

    while Q:
        (x, y, z, days) = Q.popleft()

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz

            if (
                (0 <= nx < M)
                and (0 <= ny < N)
                and (0 <= nz < H)
                and box[nz][ny][nx] == 0
            ):
                box[nz][ny][nx] = 1
                Q.append((nx, ny, nz, days + 1))
                max_days = max(days + 1, max_days)

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 0:
                    print(-1)
                    return

    print(max_days)


solution()
