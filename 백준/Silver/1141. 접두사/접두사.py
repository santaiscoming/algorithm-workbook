import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]


def solution():
    trie = {}

    def add(word):
        child = trie

        for ch in word:
            if ch not in child:
                child[ch] = {}

            child = child[ch]

    def dfs(node):
        if not node:
            return 1

        result = 0

        for v in node.values():
            result += dfs(v)

        return result

    [add(s) for s in arr]
    print(dfs(trie))


solution()
