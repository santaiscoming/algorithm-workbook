import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

ordered = []

while True:
    num = input().rstrip()
    if bool(num) == False:
        break

    ordered.append(int(num))


class Node:
    def __init__(self, key):
        self.key = key
        self.left: Node = None
        self.right: Node = None


class BST:
    def __init__(self):
        self.root: Node = None

    def insert(self, node: Node):
        if self.root is None:
            self.root = node
            return

        curr_root = self.root
        parent = None
        while True:
            if curr_root is None:
                if node.key < parent.key:
                    parent.left = node
                else:
                    parent.right = node
                break

            if node.key < curr_root.key:
                parent = curr_root
                curr_root = curr_root.left
            else:
                parent = curr_root
                curr_root = curr_root.right

    def post_print(self, node: Node):
        if node is None:
            return

        self.post_print(node.left)
        self.post_print(node.right)
        print(node.key)


def solution():
    bst = BST()

    for key in ordered:
        node = Node(key)
        bst.insert(node)

    bst.post_print(bst.root)


solution()
