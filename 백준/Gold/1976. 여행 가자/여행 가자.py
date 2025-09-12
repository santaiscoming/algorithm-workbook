import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [list(map(int, input().split(" "))) for _ in range(n)]
plan = list(map(int, input().split(" ")))


def solve():
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

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

    for start, v in enumerate(edges):
        for to, isConnect in enumerate(v):
            if bool(isConnect):
                union(start, to)

    result = "YES"
    for i in range(1, len(plan)):
        _from, to = plan[i - 1], plan[i]
        if find(_from - 1) != find(to - 1):
            result = "NO"
            break

    print(result)


solve()
