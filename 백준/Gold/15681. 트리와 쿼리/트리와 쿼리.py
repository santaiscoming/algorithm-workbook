import sys
from collections import deque

sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, r, q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
queries = [int(input()) for _ in range(q)]


def solution():
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    size = [0] * (n + 1)
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        size[node] = 1

        for v in graph[node]:
            if not visited[v]:
                dfs(v)
                size[node] += size[v]

    def bfs(root):
        children = [[] for _ in range(n + 1)]

        q = deque([root])
        visited[root] = True

        while q:
            u = q.popleft()

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    children[u].append(v)
                    q.append(v)

        def bottomUp(node):
            size[node] = 1

            for child in children[node]:
                bottomUp(child)
                size[node] += size[child]

        bottomUp(root)

    # bfs(r)
    dfs(r)

    for node in queries:
        print(size[node])


solution()
