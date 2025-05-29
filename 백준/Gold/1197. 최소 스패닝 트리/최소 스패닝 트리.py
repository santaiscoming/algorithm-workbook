import sys
from math import inf
from collections import defaultdict
from itertools import chain
import heapq

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 크루스칼은 단방향, 프림은 양방향 그래프를 갖아야 하는 이유
# 크루스칼은 간선만 생각하는 알고리즘
# 프림은 현재 정점 기준 인접한 정점을 찾아야하기 때문


def kruskalSolution():
    parent = [i for i in range(n + 1)]
    rank = [i for i in range(n + 1)]

    def find(x):
        # if parent[x] != x:
        #     parent[x] = find(parent[x])

        # return parent[x]
        root = x
        while root != parent[root]:
            root = parent[root]

        while parent[x] != root:
            p = parent[x]
            parent[x] = root
            x = p

        return root

    def union(a, b):
        v = find(a)
        w = find(b)

        if rank[v] > rank[w]:
            v, w = w, v

        parent[v] = w
        if rank[v] == rank[w]:
            rank[w] += 1

    # paths = list(chain(*[[[s, u, w], [u, s, w]] for s, u, w in edges]))
    paths = [[s, u, w] for s, u, w in edges]
    paths.sort(key=lambda x: x[2])

    result = 0

    for s, v, w in paths:
        if find(s) != find(v):
            union(s, v)
            result += w

    print(result)


kruskalSolution()


def primSolution():
    """
    356ms
    """
    cost = [inf] * (n + 1)
    parent = [None] * (n + 1)
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

    while len(T) < n - 1:
        w, u = heapq.heappop(q)

        if visited[u]:
            continue

        visited[u] = True

        if parent[u] is not None:
            T.append((u, parent[u]))
            result += w

        for v, w in graph[u]:
            if w < cost[v]:
                cost[v] = w
                parent[v] = u
                heapq.heappush(q, (w, v))

    print(result)


# primSolution()


def primWithoutCostArrSolution():
    """
    452ms
    """
    visited = [False] * (n + 1)
    visited[0] = True
    graph = defaultdict(list)
    for s, u, w in edges:
        graph[s].append((u, w))

    result = 0
    q = [[0, 1]]

    while q:
        w, u = heapq.heappop(q)

        if visited[u]:
            continue

        visited[u] = True
        result += w

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(q, (w, v))

    print(result)


# primWithoutCostArrSolution()
