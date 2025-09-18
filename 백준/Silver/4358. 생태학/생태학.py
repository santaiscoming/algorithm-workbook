import sys
from collections import Counter

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

words = [v for v in iter(lambda: input().rstrip(), "")]


def solve():
    counter = Counter(words)
    n = len(words)
    [
        print(*[v, f"{round(i / n * 100, 4):.4f}"])
        for v, i in sorted(counter.items(), key=lambda x: x)
    ]


solve()
