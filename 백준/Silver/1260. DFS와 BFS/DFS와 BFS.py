import sys
import copy
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, M, V = map(int, input().split())

vertexes = [list(map(int, input().split())) for _ in range(M)]
graph = {i: [] for i in range(1, N + 1)}

for vertex_1, vertex_2 in vertexes:
    graph[vertex_1].append(vertex_2)
    graph[vertex_2].append(vertex_1)


def dfs(graph, start, N):
    visited = [False] * (N + 1)
    result = []

    def _dfs(node):
        visited[node] = True
        result.append(node)

        for child in sorted(graph[node]):
            if visited[child]:
                continue

            _dfs(child)

    _dfs(start)
    return result


def bfs(graph, start, N):
    visited = [False] * (N + 1)
    result = []
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        curr_node = q.popleft()
        result.append(curr_node)
        for adj_node in sorted(graph[curr_node]):
            if visited[adj_node]:
                continue
            q.append(adj_node)
            visited[adj_node] = True

    return result


def solution(graph, start, N):
    visited = [False] * (N + 1)

    dfs_result = dfs(graph, start, N)
    bfs_result = bfs(graph, start, N)

    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))


solution(graph, V, N)
