import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

tc = int(input())
inputs = []

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, v, t = list(map(int, input().split()))
        edges.append([s, v, t])
        edges.append([v, s, t])
    wormholes = []
    for _ in range(w):
        s, v, t = list(map(int, input().split()))
        edges.append([s, v, -t])

    inputs.append((n, m, w, edges))


def solution():
    for n, m, w, edges in inputs:
        dist = [0] * (n + 1)
        result = False

        for _ in range(n):
            for u, v, w in edges:
                dist[v] = min(dist[v], dist[u] + w)

        result = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                result = True
                break

        print("YES") if result else print("NO")


solution()
