import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
stringSet = [input().strip() for _ in range(n)]
searchStrings = [input().strip() for _ in range(m)]


def solution():
    class Node:
        def __init__(self) -> None:
            self.child = {}
            self.isEnd = False

        def setIsEnd(self, bool):
            self.isEnd = bool

    class Trie:
        def __init__(self) -> None:
            self.root = Node()

        def add(self, word):
            node = self.root

            for ch in word:
                node = node.child.setdefault(ch, Node())

            node.setIsEnd(True)

        def search(self, word) -> bool:
            node = self.root

            for ch in word:
                if ch not in node.child:
                    return False

                node = node.child[ch]

            return node.isEnd

    trie = Trie()
    [trie.add(s) for s in stringSet]
    print(sum(trie.search(s) for s in searchStrings))


solution()
