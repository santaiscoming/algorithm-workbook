import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


def solution():
    dist = [math.inf] * (n + 1)
    dist[1] = 0

    for _ in range(n):
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    is_negative_cycle = False
    for u, v, w in edges:
        if dist[v] > dist[u] + w:
            is_negative_cycle = True
            break

    if is_negative_cycle:
        print(-1)
    else:
        for d in dist[2:]:
            print(-1) if d == math.inf else print(d)


solution()
