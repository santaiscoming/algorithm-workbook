import sys
import math

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
m = int(input())

edges = [[int(x) for x in input().split()] for _ in range(m)]


def fSolution():
    graph = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0
    for s, v, w in edges:
        if graph[s][v] > w:
            graph[s][v] = w

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for idx, row in enumerate(graph):
        if idx == 0:
            continue
        for i in range(1, n + 1):
            if graph[idx][i] == math.inf:
                graph[idx][i] = 0

        print(*row[1:])


fSolution()


def dSolution():
    pass
