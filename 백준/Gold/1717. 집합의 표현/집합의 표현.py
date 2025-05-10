import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]


def solution():
    class Node:
        def __init__(self, key):
            self.key = key
            self.parent = self
            self.rank = 0

    def find(x: Node):
        if x != x.parent:
            x.parent = find(x.parent)
        return x.parent

    def union(x: Node, y: Node):
        x = find(x)
        y = find(y)
        if x.rank > y.rank:
            x, y = y, x
        y.parent = x

        if x.rank == y.rank:
            y.rank += 1

    sets = [Node(i) for i in range(n + 1)]

    for a, b, c in arr:
        if a == 0:
            union(sets[b], sets[c])
        else:
            print("YES" if find(sets[b]) == find(sets[c]) else "NO")


solution()
