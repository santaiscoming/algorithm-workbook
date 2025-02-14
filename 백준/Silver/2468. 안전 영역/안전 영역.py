import sys


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]


def solution():
    result = []
    maximum_height = max(map(max, mat))

    def safety_zone(water_height):
        visited = [[False] * N for _ in range(N)]
        cnt = 0
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for y in range(N):
            for x in range(N):
                if mat[y][x] < water_height:
                    visited[y][x] = True

        def dfs(x, y):
            visited[y][x] = True

            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if not visited[ny][nx]:
                    dfs(nx, ny)

        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    dfs(x, y)
                    cnt += 1

        result.append(cnt)

    for i in range(maximum_height + 1):
        safety_zone(water_height=i)

    print(max(result))


solution()
