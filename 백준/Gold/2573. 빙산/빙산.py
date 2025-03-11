import sys
import copy
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def solution():
    global mat
    year = 0

    def getMeltCount(mat, x, y):
        result = 0

        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N and mat[ny][nx] == 0:
                result += 1

        return result

    def melt(mat):
        copiedMat = [row[:] for row in mat]

        for y in range(N):
            for x in range(M):
                if copiedMat[y][x] > 0:
                    copiedMat[y][x] = max(copiedMat[y][x] - getMeltCount(mat, x, y), 0)

        return copiedMat

    def bfs(x, y, mat, visited):
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for dx, dy in dir:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < M
                    and 0 <= ny < N
                    and not visited[ny][nx]
                    and mat[ny][nx] > 0
                ):
                    visited[ny][nx] = True
                    q.append((nx, ny))

    def getContinentCnt(mat):
        visited = [[False] * M for _ in range(N)]
        result = 0

        for y in range(N):
            for x in range(M):
                if not visited[y][x] and mat[y][x] != 0:
                    bfs(x, y, mat, visited)
                    visited[y][x] = True
                    result += 1

        return result

    while True:
        continentCnt = getContinentCnt(mat)
        if continentCnt == 0:
            print(0)
            return

        if continentCnt >= 2:
            print(year)
            return

        mat = melt(mat)
        year += 1


solution()
