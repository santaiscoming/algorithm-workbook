import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

t = int(input())
tcs = [[input().rstrip() for _ in range(int(input()))] for _ in range(t)]


def solution():
    for words in tcs:

        trie = {}

        def printTrie(node, depth, word):
            if "END" in node:
                print(" " * depth + word + "(단어)")

            for ch in sorted(k for k in node if k != "END"):
                print(" " * depth + word + ch)
                printTrie(node[ch], depth + 1, word + ch)

        def add(word) -> bool:
            node = trie

            for ch in word:
                node = node.setdefault(ch, {})

            node["END"] = True

            if len(node) > 1:
                return False

            return True

        isValid = True
        for word in sorted(words, key=len, reverse=True):
            if not add(word):
                isValid = False

        print("YES") if isValid else print("NO")


solution()
