import sys
from itertools import combinations

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

s = input().rstrip()


def solution():
    def createLps(pattern):
        n = len(pattern)
        lps = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        return lps

    result = 0

    for i in range(len(s)):
        ns = s[i:]
        lps = createLps(ns)
        result = max(result, max(lps))

    print(result)


solution()
