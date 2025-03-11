import sys
from collections import deque

# sys.stdin = open("./input.txt", "r")  # 제출 전 제거
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 이동
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS를 이용해 하나의 연결된 빙산 영역을 탐색하는 함수
def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# 현재 격자에서 빙산의 연결 컴포넌트 수를 구하는 함수
def count_components():
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    return count

# 빙산 녹는 과정을 시뮬레이션하는 함수 (동시에 녹아야 하므로 복사본 사용)
def melt():
    new_grid = [row[:] for row in grid]  # grid 복사
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                water_count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 0:
                            water_count += 1
                # 현재 높이에서 인접한 물의 개수만큼 빙산이 녹음 (음수 방지)
                new_grid[i][j] = max(grid[i][j] - water_count, 0)
    return new_grid

year = 0

while True:
    # 현재 빙산이 몇 개의 연결 컴포넌트로 이루어져 있는지 확인
    comps = count_components()
    if comps >= 2:
        print(year)
        break
    if comps == 0:
        print(0)
        break
    # 한 해 동안 빙산이 녹는 과정 시뮬레이션
    grid = melt()
    year += 1