import sys
from math import inf
from collections import defaultdict
import heapq

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


def primSolution():
    cost = [inf] * (n + 1)
    E = [None] * (n + 1)
    visited = [False] * (n + 1)
    graph = defaultdict(list)
    for s, u, w in edges:
        graph[s].append((u, w))
        graph[u].append((s, w))

    result = 0
    T = []

    q = []
    for i in range(1, n + 1):
        heapq.heappush(q, (cost[i], i))

    while q and len(T) < n - 1:
        w, u = heapq.heappop(q)
        if visited[u]:
            continue

        visited[u] = True

        if E[u] is not None:
            T.append((u, E[u]))
            result += w

        for v, w in graph[u]:
            if w < cost[v]:
                cost[v] = w
                E[v] = u
                heapq.heappush(q, (w, v))

    print(result)


primSolution()
