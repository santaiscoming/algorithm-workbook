import sys
from typing import Dict

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

tcs = []
while True:
    try:
        n = int(input())
        tcs.append([input().rstrip() for _ in range(n)])
    except:
        break


def solution():
    class Node:
        def __init__(self):
            self.child: Dict[str, Node] = {}
            self.isEnd = False

        def setIsEnd(self, bool):
            self.isEnd = bool

    class Trie:
        def __init__(self):
            self.root = Node()

        def add(self, word):
            node = self.root

            for c in word:
                if c not in node.child:
                    node.child[c] = Node()
                node = node.child[c]

            node.setIsEnd(True)

        def search(self, word):
            node = self.root

            for c in word:
                if c not in node.child:
                    return False

                node = node.child[c]

            return node.isEnd

        def getClickCount(self, word):
            result = 0

            def click():
                nonlocal result
                result += 1

            node = self.root

            for i, c in enumerate(word):
                if i == 0:
                    click()
                    node = node.child[c]
                    continue

                if len(node.child) > 1 or node.isEnd:
                    click()

                node = node.child[c]

            return result

        def print(self):
            def dfs(node: Node, word, depth):
                if node.isEnd:
                    print(" " * depth + word + "(단어)", node.isEnd)

                for k in sorted(node.child.keys()):
                    print(" " * depth + word)
                    dfs(node.child[k], word + k, depth + 1)

            dfs(self.root, "", 0)

    for tc in tcs:
        trie = Trie()
        result = []

        for word in tc:
            trie.add(word)

        for word in tc:
            result.append(trie.getClickCount(word))

        print(f"{sum(result) / len(result):.2f}")


solution()
