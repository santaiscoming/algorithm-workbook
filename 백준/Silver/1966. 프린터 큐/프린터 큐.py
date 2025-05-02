import sys
from collections import deque

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
inputs = [
    (list(map(int, input().split())), list(map(int, input().split()))) for _ in range(n)
]


def solution():
    def QPrinter(info, priorities):
        n, m = info
        papers = [(i, priorities[i]) for i in range(n)]
        arr = sorted(priorities, reverse=True)
        hp = max(arr)
        count = 0

        processQ = deque(papers)

        while True:
            v = processQ.popleft()
            i, p = v

            if p == hp:
                if i == m:
                    return count + 1

                count += 1
                hp = max(arr[count:])
                continue

            processQ.append(v)

    for v in inputs:
        info, priorities = v
        print(QPrinter(info, priorities))


solution()
