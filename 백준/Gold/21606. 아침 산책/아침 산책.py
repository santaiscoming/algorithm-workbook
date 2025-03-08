import sys
from itertools import combinations, permutations

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
str = "2" + input().rstrip()
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]


def solution():
    cnt = 0
    visited = [False] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append((v, bool(int(str[v]))))
        graph[v].append((u, bool(int(str[u]))))

    def dfs(start):
        nonlocal cnt

        for edge in graph[start]:
            v, isInside = edge

            if isInside and not visited[v]:
                cnt += 1
            elif not visited[v] and not isInside:
                visited[v] = True
                dfs(v)
                visited[v] = False

    for s in range(1, N + 1):
        if str[s] == "1":
            visited[s] = True
            dfs(s)
            visited[s] = False

    print(cnt)


solution()
