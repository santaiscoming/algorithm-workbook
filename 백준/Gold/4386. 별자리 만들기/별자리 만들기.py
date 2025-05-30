import sys
import math
from collections import defaultdict
import heapq

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
axises = [tuple(map(float, input().split())) for _ in range(n)]


def solution():
    def getDist(x1, y1, x2, y2):
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

    cost = {}
    visited = {}
    parent = {}
    for axis in axises:
        cost[axis] = math.inf
        visited[axis] = False
        parent[axis] = None

    T = []
    q = []
    heapq.heappush(q, (cost[axises[0]], axises[0]))

    while len(T) < n and q:
        w, u = heapq.heappop(q)

        if visited[u]:
            continue

        visited[u] = True

        if parent[u] is not None:
            T.append(w)

        for v in axises:
            if u == v:
                continue

            dist = getDist(*u, *v)

            if dist < cost[v]:
                heapq.heappush(q, (dist, v))
                parent[v] = u

    print(sum(T))


solution()
