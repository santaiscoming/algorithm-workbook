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
    dir = [[0, -1, 0], [1, 0, 0], [0, 1, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]
    q = deque()
    max_days = 0

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    q.append((x, y, z, 0))

    while q:
        x, y, z, days = q.popleft()
        max_days = max(max_days, days)

        for dx, dy, dz in dir:
            nx, ny, nz = x + dx, y + dy, z + dz

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = 1
                    q.append((nx, ny, nz, days + 1))

    for h in range(H):
        for y in range(N):
            for x in range(M):
                if box[h][y][x] == 0:
                    print(-1)
                    return

    print(max_days)


solution()
