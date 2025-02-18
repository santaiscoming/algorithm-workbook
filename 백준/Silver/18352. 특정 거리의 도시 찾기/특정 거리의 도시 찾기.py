import sys
import heapq
import math
from typing import Dict, List

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(M)]


def solution():
    graph: Dict[int, List[int]] = {}
    for u, v in edges:
        u, v = u - 1, v - 1
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)

    s = X - 1
    dist = [math.inf] * N
    dist[s] = 0
    parent = [None] * N
    q = [(dist[s], s)]

    def weight(u, v):
        return 1

    while q:
        d, u = heapq.heappop(q)
        if u not in graph:
            continue
        for v in graph[u]:
            if dist[v] > d + weight(u, v):
                dist[v] = d + weight(u, v)
                parent[v] = u
                heapq.heappush(q, (dist[v], v))

    result = []
    for i in range(N):
        if dist[i] == K:
            result.append(i + 1)

    [print(d) for d in sorted(result)]

    if not result:
        print(-1)


solution()
