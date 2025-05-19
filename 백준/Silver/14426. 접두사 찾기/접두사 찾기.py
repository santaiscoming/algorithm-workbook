import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())

stringSets = [input().rstrip() for _ in range(n)]
searchWords = [input().rstrip() for _ in range(m)]


def solution():
    trie = {}

    for s in stringSets:
        node = trie
        for ch in s:
            node = node.setdefault(ch, {})

        node["END"] = True

    result = 0

    for word in searchWords:
        node = trie
        isPrefix = True

        for ch in word:
            if ch not in node:
                isPrefix = False
                break

            node = node[ch]

        if isPrefix:
            result += 1

    print(result)


solution()
