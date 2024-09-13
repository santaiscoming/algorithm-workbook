import sys
from functools import reduce
from collections import Counter

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().rstrip() for _ in range(N)]


def solution(N, M, words):
    frequency_map = Counter(words)

    result = sorted(
        filter(lambda x: len(x) >= M, frequency_map.keys()),
        key=lambda x: (-frequency_map[x], -len(x), x),
    )

    for word in result:
        print(word)


solution(N, M, words)
