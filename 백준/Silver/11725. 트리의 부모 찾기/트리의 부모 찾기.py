import sys

sys.setrecursionlimit(10**6)
# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]


def solution():
    visited = [False] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    parent = [None] * (N + 1)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(start):
        if start >= N + 1:
            return

        for v in graph[start]:
            if not visited[v]:
                visited[v] = True
                parent[v] = start
                dfs(v)

    dfs(1)

    for i in range(2, len(parent)):
        print(parent[i])


solution()
