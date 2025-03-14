import sys
from collections import deque

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


def solution():
    """
    # in-deg 테이블을 만든다
    # in-deg가 0인 v를 배열에 넣고 방문한다 (arr for 0 in-deg)
    # v와 연결된 정점의 in-deg를 감소시킨다
    # 만약 indeg가 0이라면 queue에 넣는다
    """

    result = []
    inDegTable = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    inDegTable[0] = -1
    q = deque()

    for s, v in edges:
        inDegTable[v] += 1
        graph[s].append(v)

    for s, inDeg in enumerate(inDegTable):
        if inDeg == 0:
            q.append(s)

    while q:
        u = q.popleft()
        result.append(u)

        for v in graph[u]:
            inDegTable[v] -= 1

            if inDegTable[v] == 0:
                q.append(v)

    print(*result)


solution()
