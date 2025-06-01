import sys
from collections import deque

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution():
    def makeUnionFind(n):
        parent = [*range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            v, w = find(a), find(b)

            if rank[v] > rank[w]:
                v, w = w, v
            parent[v] = w

            if rank[v] == rank[w]:
                rank[w] += 1

        return union, find

    def bfs(sx, sy, visited):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        q.append((sx, sy))
        visited[sy][sx] = True

        axises = []
        axises.append((sx, sy))

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and not visited[ny][nx]
                    and mat[ny][nx] == 1
                ):
                    axises.append((nx, ny))
                    q.append((nx, ny))
                    visited[ny][nx] = True

        return axises

    visited = [[False] * m for _ in range(n)]
    axises = []
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and mat[y][x] == 1:
                islandAxis = bfs(x, y, visited)
                axises.append(islandAxis)

    def isCrossIsland(x1, y1, x2, y2):
        result = True

        if x1 == x2:
            if y1 < y2:
                for ny in range(y1 + 1, y2):
                    if mat[ny][x1] == 1:
                        result = False
                        break
            else:
                for ny in range(y2 + 1, y1):
                    if mat[ny][x1] == 1:
                        result = False
                        break

        elif y1 == y2:
            if x1 < x2:
                for nx in range(x1 + 1, x2):
                    if mat[y1][nx] == 1:
                        result = False
                        break
            else:
                for nx in range(x2 + 1, x1):
                    if mat[y1][nx] == 1:
                        result = False
                        break

        return result

    islandCnt = len(axises)
    edges = []
    for i in range(islandCnt):
        island1 = axises[i]
        for j in range(i + 1, islandCnt):
            island2 = axises[j]
            key1, key2 = i, j

            for x1, y1 in island1:
                for x2, y2 in island2:
                    bridgeSize = None
                    if not isCrossIsland(x1, y1, x2, y2):
                        continue

                    if x1 == x2:  # 세로로 다리를 놓을 수 있음
                        if y1 < y2:
                            if (
                                y1 + 1 < n
                                and mat[y1 + 1][x1] == 0
                                and y2 - 1 >= 0
                                and mat[y2 - 1][x1] == 0
                            ):
                                bridgeSize = abs(y2 - y1) - 1
                        else:
                            if (
                                y2 + 1 < n
                                and mat[y2 + 1][x1] == 0
                                and y1 - 1 >= 0
                                and mat[y1 - 1][x1] == 0
                            ):
                                bridgeSize = abs(y2 - y1) - 1
                    elif y1 == y2:  # 가로로 다리를 놓을 수 있음
                        if x1 < x2:
                            if (
                                x1 + 1 < m
                                and mat[y1][x1 + 1] == 0
                                and x2 - 1 >= 0
                                and mat[y1][x2 - 1] == 0
                            ):
                                bridgeSize = abs(x2 - x1) - 1
                        else:
                            if (
                                x2 + 1 < m
                                and mat[y1][x2 + 1] == 0
                                and x1 - 1 >= 0
                                and mat[y1][x1 - 1] == 0
                            ):
                                bridgeSize = abs(x2 - x1) - 1

                    if bridgeSize is not None and bridgeSize >= 2:
                        edges.append([bridgeSize, key1, key2, (x1, y1), (x2, y2)])
                        # print(x1, y1, x2, y2, "-", bridgeSize)

    union, find = makeUnionFind(islandCnt)

    result = 0
    edges.sort(key=lambda x: x[0])
    mstEdgeCnt = 0
    for w, u, v, i1, i2 in edges:
        if find(u) != find(v):
            union(u, v)
            mstEdgeCnt += 1
            # print(w, u, v, i1, i2, "걸")
            result += w

    if mstEdgeCnt == islandCnt - 1:
        print(result)
    else:
        print(-1)


solution()
