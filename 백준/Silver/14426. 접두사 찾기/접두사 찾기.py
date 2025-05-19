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


# solution()

from bisect import bisect_left


def solution2():
    S = sorted(stringSets)
    bound = len(S)
    result = 0

    for word in searchWords:
        idx = bisect_left(S, word)

        if idx >= bound:
            continue

        if S[idx].startswith(word):
            result += 1

    print(result)


solution2()
