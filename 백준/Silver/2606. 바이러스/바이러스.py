import sys
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

com_cnt = int(input())
com_edge_cnt = int(input())
com_connect = [list(map(int, input().split())) for _ in range(com_edge_cnt)]
graph = [[] for _ in range(com_cnt + 1)]


for v1, v2 in com_connect:
    graph[v1].append(v2)
    graph[v2].append(v1)

    
def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur_v = q.popleft()
        visited[cur_v] = True

        for adj_v in graph[cur_v]:
            if visited[adj_v]:
                continue
            q.append(adj_v)


def solution(graph):
    infection = [False] * (com_cnt + 1)

    bfs(graph, 1, infection)

    print(len(list(filter(lambda x: x == True, infection))) - 1)


solution(graph)
