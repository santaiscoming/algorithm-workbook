import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
ways = [tuple(map(int, input().split())) for _ in range(m)]


def solution():
    def makeUnionFind(n):
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            v, w = find(x), find(y)

            if rank[v] > rank[w]:
                v, w = w, v
            parent[v] = w

            if rank[v] == rank[w]:
                rank[w] += 1

        return union, find

    def calcDist(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    edges = [
        [i + 1, j + 1, calcDist(*points[i], *points[j])]
        for i in range(n)
        for j in range(i + 1, n)
    ]
    edges.sort(key=lambda x: x[2])
    union, find = makeUnionFind(n)

    for u, v in ways:
        union(u, v)

    result = 0
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            result += w

    print(f"{round(result, 2):.2f}")


solution()
