import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


def solution():
    parent = [i for i in range(n + 1)]
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
        rank[w] += 1

    result = 0
    houses = 1

    for a, b, c in sorted(edges, key=lambda x: x[2]):
        if houses == n - 1:
            break

        if find(a) != find(b):
            union(a, b)
            result += c
            houses += 1

    print(result)


solution()
