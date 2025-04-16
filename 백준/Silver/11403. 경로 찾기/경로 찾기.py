import sys
from collections import deque

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
adj_mat = [list(map(int, input().split())) for _ in range(n)]


def solution():
    result = [[0] * n for _ in range(n)]

    def bfs(s, _from, depth):
        visited = [[False] * n for _ in range(n)]
        q = deque()
        q.append((s, _from, depth))

        while q:
            u, f, d = q.popleft()

            for v in range(n):
                if u == v:
                    continue

                if f == v and d > 0 and adj_mat[u][v] == 1:
                    visited[f][f] = True
                    result[f][f] = 1
                    continue

                if not visited[u][v] and adj_mat[u][v] == 1:
                    visited[u][v] = True
                    result[u][v] = 1
                    result[_from][v] = 1
                    q.append((v, f, d + 1))

    for s in range(n):
        bfs(s, s, 0)

    for v in result:
        print(*v)


solution()
