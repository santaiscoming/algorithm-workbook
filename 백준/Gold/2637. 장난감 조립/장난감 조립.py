import sys
from collections import deque, defaultdict

# sys.stdin = open("./input.txt", "r")  # 제출 시 제거
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]


def solution():
    graph = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)
    for x, y, w in edges:
        graph[y].append((x, w))
        inDegree[x] += 1

    parts = {}
    defaultParts = [i for i, v in enumerate(inDegree) if i != 0 and v == 0]
    for defaultPart in defaultParts:
        parts[defaultPart] = {defaultPart: 1}

    q = deque(defaultParts)

    while q:
        u = q.popleft()

        # print(f"u -> {u}")
        for v, w in graph[u]:
            # print(f"  v->{v} w->{w}")
            # print(f"  beforeP:{parts}")

            for part, cnt in parts[u].items():
                if not v in parts:
                    parts[v] = {}

                if not part in parts[v]:
                    parts[v][part] = 0

                parts[v][part] += cnt * w
            # print(f"  afterP:{parts}")

            # print(f"  updateP:{parts}")

            inDegree[v] -= 1

            if inDegree[v] == 0:
                q.append(v)

    [print(k, v) for k, v in sorted(parts[n].items())]


solution()
