import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

tcs = []
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    edges = [list(map(int, input().split())) for _ in range(m)]
    tcs.append((n, m, edges))


def solution(n, m, edges):
    def makeUnionFind(n):
        parent = [*range(n + 1)]
        rank = [0] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            v, w = find(a), find(b)

            if rank[v] > rank[w]:
                v, w = w, v
            parent[v] = w

            if rank[v] == rank[w]:
                rank[w] += 1

        return union, find

    union, find = makeUnionFind(n)

    edges.sort(key=lambda x: x[2])
    edgeSets = set(map(tuple, edges))

    for a, b, w in edges:
        if find(a) != find(b):
            union(a, b)
            edgeSets.remove((a, b, w))

    print(sum(w for _, _, w in edgeSets))


for n, m, edges in tcs:
    solution(n, m, edges)
