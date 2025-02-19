import sys
from typing import Dict, Tuple, List
import heapq
import math

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = [map(int, input().split()) for _ in range(M)]
start, dest = map(int, input().split())
graph: Dict[int, List[Tuple[int, int]]] = {}
[graph.setdefault(v - 1, []).append((w, u - 1)) for v, u, w in edges]


def solution(start, dest):
    s, d = start - 1, dest - 1
    dist = [math.inf] * N
    dist[s] = 0
    q = []

    heapq.heappush(q, (dist[s], s))

    while q:
        uw, u = heapq.heappop(q)
        if u not in graph or uw > dist[u]:
            continue

        for vw, v in graph[u]:
            if dist[v] > dist[u] + vw:
                dist[v] = dist[u] + vw
                heapq.heappush(q, (dist[v], v))

    print(dist[d])


solution(start, dest)
