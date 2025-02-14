import sys
from collections import deque


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]


def solution():
    result = []
    maximum_height = max(map(max, mat))
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(y, x, visited):
        q = deque()
        q.append((y, x))

        while q:
            (y, x) = q.popleft()

            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if ny < 0 or nx < 0 or ny >= N or nx >= N:
                    continue

                if not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

    def get_safety_zone_count(water_height):
        visited = [
            [True if mat[y][x] < water_height else False for x in range(N)]
            for y in range(N)
        ]
        cnt = 0

        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    bfs(y, x, visited)
                    cnt += 1

        return cnt

    # def dfs(x, y, visited):
    #     visited[y][x] = True

    #     for dx, dy in dir:
    #         nx, ny = x + dx, y + dy
    #         if nx < 0 or ny < 0 or nx >= N or ny >= N:
    #             continue

    #         if not visited[ny][nx]:
    #             dfs(nx, ny, visited)

    # def get_safety_zone_count(water_height):
    #     visited = [[False] * N for _ in range(N)]
    #     cnt = 0

    #     for y in range(N):
    #         for x in range(N):
    #             if mat[y][x] < water_height:
    #                 visited[y][x] = True

    #     for y in range(N):
    #         for x in range(N):
    #             if not visited[y][x]:
    #                 dfs(x, y, visited)
    #                 cnt += 1

    #     return cnt

    for i in range(maximum_height + 1):
        result.append(get_safety_zone_count(i))

    print(max(result))


solution()
