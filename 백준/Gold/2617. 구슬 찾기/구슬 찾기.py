import sys

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]


def solution():
    heavyGraph = [[] for _ in range(N + 1)]
    lightGraph = [[] for _ in range(N + 1)]
    for s, v in edges:
        heavyGraph[s].append(v)
        lightGraph[v].append(s)

    result = 0

    def dfs(start, graph, visited):
        cnt = 0
        visited[start] = True

        for u in graph[start]:
            if not visited[u]:
                cnt += dfs(u, graph, visited) + 1

        return cnt

    for i in range(1, N + 1):
        visitedLight = [False] * (N + 1)
        lightCnt = dfs(i, lightGraph, visitedLight)
        visitedHeavy = [False] * (N + 1)
        heavyCnt = dfs(i, heavyGraph, visitedHeavy)

        ThresholdCnt = (N + 1) // 2
        if lightCnt >= ThresholdCnt or heavyCnt >= ThresholdCnt:
            result += 1

    print(result)


solution()
