import sys
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
edge_info = [list(map(int, input().split())) for _ in range(N - 1)]


def dfs(graph, start, visited, result):
    if visited[start]:
        return

    visited[start] = True

    for adj_v in graph[start]:
        if visited[adj_v]:
            continue
        result[adj_v] = start
        dfs(graph, adj_v, visited, result)


def solution(edge_info, N):
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    result = [0] * (N + 1)

    for v1, v2 in edge_info:
        graph[v1].append(v2)
        graph[v2].append(v1)

    dfs(graph, 1, visited, result)

    for i, parent in enumerate(result):
        if i == 0 or i == 1:
            continue

        print(parent)


solution(edge_info, N)
