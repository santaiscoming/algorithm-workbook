import sys
from typing import List
from collections import defaultdict, deque

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
tcs = []
for _ in range(n):
    f = int(input())
    tcs.append([input().split() for _ in range(f)])


def solution():
    def find(x: str):
        root = x
        while root != parent[root]:
            root = parent[root]

        while x != parent[x]:
            p = parent[x]
            parent[x] = root
            x = p

        return root

    def union(x: str, y: str):
        v, w = find(x), find(y)

        if rank[v] > rank[w]:
            v, w = w, v
        parent[v] = w
        size[w] += size[v]

        if rank[v] == rank[w]:
            rank[w] += 1

        return size[w]

    for tc in tcs:
        parent = {}
        rank = {}
        size = {}

        for a, b in tc:
            if a not in parent:
                parent[a] = a
                rank[a] = 0
                size[a] = 1
            if b not in parent:
                parent[b] = b
                rank[b] = 0
                size[b] = 1

            if find(a) != find(b):
                cnt = union(a, b)
                print(cnt)
            else:
                print(size[parent[b]])


solution()
