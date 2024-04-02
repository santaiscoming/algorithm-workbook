import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]


def dfs(graph, start, visited):
    if visited[start]:
        return

    visited[start] = True

    for adj in graph[start]:
        if visited[adj]:
            continue

        dfs(graph, adj, visited)


def solution(edges):
    # 모든 정점을 돌면서 bfs를 돌린다
    # bfs 한바퀴를 돌면 다른 요소에 대해 돌아도 돌지 않을것이다.
    visited = [False] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    result = 0

    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, N + 1):
        if visited[i]:
            continue
        dfs(graph, i, visited)
        result += 1

    return result


result = solution(edges)
print(result)
