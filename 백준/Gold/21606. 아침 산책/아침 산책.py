import sys
from itertools import combinations, permutations

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
strArr = list(input().rstrip())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]


def solution():
    cnt = 0
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for u, v in edges:
        graph[u].append((v, bool(int(strArr[v - 1]))))
        graph[v].append((u, bool(int(strArr[u - 1]))))

    combi = list(permutations([x + 1 for x in range(N)], 2))

    def cmp(edge):
        u, v = edge

        if strArr[u - 1] == "1" and strArr[v - 1] == "1":
            return True

        return False

    routes = list(filter(cmp, combi))

    def dfs(start, end):
        nonlocal cnt

        for edge in graph[start]:
            v, isInside = edge
            if end == v and strArr[v - 1] == "1":
                cnt += 1
                continue
            if not visited[v] and not isInside:

                visited[v] = True
                dfs(v, end)
                visited[v] = False

    for route in routes:
        s, v = route

        visited[s] = True
        dfs(s, v)
        visited[s] = False

    print(cnt)


solution()
