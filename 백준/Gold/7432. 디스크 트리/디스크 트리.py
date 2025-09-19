import sys
from collections import defaultdict

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
lines = [input().rstrip() for _ in range(n)]


def solve():
    class Node:
        def __init__(self):
            self.children = {}

    root = Node()

    for line in lines:
        cur = root
        for name in line.split("\\"):
            cur = cur.children.setdefault(name, Node())

    def dfs(node: Node, depth: int):
        for name in sorted(node.children.keys()):
            print(" " * depth + name)
            dfs(node.children[name], depth + 1)

    dfs(root, 0)


solve()
