import sys
from collections import Counter

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
words = [input().rstrip() for _ in range(N)]


def solution(N, M, words):
    filtered_words = [word for word in words if len(word) >= M]

    frequency_map = Counter(filtered_words)

    sorted_words = sorted(
        frequency_map.keys(), key=lambda x: (-frequency_map[x], -len(x), x)
    )

    for word in sorted_words:
        print(word)


solution(N, M, words)
