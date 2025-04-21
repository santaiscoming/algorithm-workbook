import sys
from collections import deque
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


def bfs_solution():
    graph = [[] for _ in range(n)]
    for s, v in edges:
        graph[s - 1].append(v - 1)
        graph[v - 1].append(s - 1)

    def bfs(start):
        result = [0] * n
        visited = [False] * n
        visited[start] = True

        q = deque([start])

        while q:
            s = q.popleft()

            for v in graph[s]:
                if not visited[v]:
                    result[v] = result[s] + 1
                    visited[v] = True
                    q.append(v)

        return sum(v for v in result)

    kevin_rate = [(i + 1, bfs(i)) for i in range(n)]
    print(min(kevin_rate, key=lambda x: (x[1], x[0]))[0])


bfs_solution()


def solution():
    dp = [[math.inf] * (n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for s, v in edges:
        dp[s - 1][v - 1] = 1
        dp[v - 1][s - 1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    kevin_rate = [0] * n
    for i in range(n):
        for j in range(n):
            tmp = min(dp[i][j], dp[j][i])

            if tmp != math.inf:
                kevin_rate[i] += tmp

    print(kevin_rate.index(min(kevin_rate)) + 1)


# solution()
