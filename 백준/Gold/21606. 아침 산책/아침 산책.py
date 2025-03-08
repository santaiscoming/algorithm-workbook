import sys

sys.setrecursionlimit(10**6)

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
inside = "2" + input().rstrip()
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]


def solution():
    result = 0
    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append((v, bool(int(inside[v]))))
        graph[v].append((u, bool(int(inside[u]))))
        if inside[u] == "1" and inside[v] == "1":
            result += 2
    visited = [False] * (N + 1)

    def dfs(start):
        inNodeCnt = 0

        for neighbor in graph[start]:
            v, isInside = neighbor

            if isInside:
                inNodeCnt += 1
            elif not visited[v] and not isInside:
                visited[v] = True
                inNodeCnt += dfs(v)

        return inNodeCnt

    for s in range(1, N + 1):
        if inside[s] == "0" and not visited[s]:
            visited[s] = True
            nodeCnt = dfs(s)
            result += nodeCnt * (nodeCnt - 1)

    print(result)


solution()
