import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]


def solution2():
    parent = list(range(n + 1))
    rank = [0 for _ in range(n + 1)]

    def find(x: int):
        while x != parent[x]:
            x = parent[x]

        return x

    def union(x, y):
        v, w = find(x), find(y)
        vr, vw = rank[v], rank[w]

        if vr > vw:
            v, w = w, v

        parent[v] = w

        if vr == vw:
            rank[w] += 1

    for op, a, b in arr:
        if op == 0:
            union(a, b)
        else:
            print("YES") if find(a) == find(b) else print("NO")


solution2()


def solution():
    class Node:
        def __init__(self, key: int):
            self.parent = self
            self.key = key
            self.rank = 0

    def find(x: Node):
        while x != x.parent:
            x = x.parent

        return x

    def union(x: Node, y: Node):
        v, w = find(x), find(y)

        if v.rank > w.rank:
            v, w = w, v
        v.parent = w

        if v.rank == w.rank:
            w.rank += 1

    sets = {}

    for op, a, b in arr:
        if a not in sets:
            sets[a] = Node(a)
        if b not in sets:
            sets[b] = Node(b)

        if op == 0:
            union(sets[a], sets[b])
        else:
            print("NO") if find(sets[a]) != find(sets[b]) else print("YES")


# solution()
