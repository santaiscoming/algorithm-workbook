import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
arr = [
    list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(n)
]


def solution():
    class Node:
        def __init__(self, key, depth) -> None:
            self.key = key
            self.child = {}
            self.depth = depth

    class Trie:
        def __init__(self) -> None:
            self.root = Node(None, 0)

        def add(self, foods):
            curNode = self.root

            for food in foods:
                if curNode.child.get(food) is None:
                    curNode.child[food] = Node(food, curNode.depth + 1)
                    curNode = curNode.child[food]
                else:
                    curNode = curNode.child[food]

        def __print(self, node: Node):
            prefix = "--"
            print(f"{prefix * (node.depth - 1)}{node.key}")
            for k, v in sorted(node.child.items()):
                self.__print(v)

        def print(self):
            for _, v in sorted(self.root.child.items()):
                self.__print(v)

    trie = Trie()

    for _, *info in arr:
        trie.add(info)

    trie.print()


solution()
