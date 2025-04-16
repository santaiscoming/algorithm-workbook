import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def solution():
    def bfs(start):
        visited = [False] * n
        queue = deque([start])

        while queue:
            now = queue.popleft()
            for i in range(n):
                if graph[now][i] == 1 and not visited[i]:
                    visited[i] = True
                    result[start][i] = 1
                    queue.append(i)

    for i in range(n):
        bfs(i)

    for row in result:
        print(*row)
        
solution()