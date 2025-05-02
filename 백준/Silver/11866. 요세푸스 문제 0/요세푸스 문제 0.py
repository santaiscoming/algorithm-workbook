import sys
from collections import deque


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())


def solution():
    result = []
    q = deque(list(range(1, n + 1)))
    while len(q) != 0:

        for _ in range(k - 1):
            v = q.popleft()
            q.append(v)

        result.append(q.popleft())

    print("<" + ", ".join(map(str, result)) + ">")


solution()
