import math
import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]


def solution():
    result = math.inf
    visited = [False] * N

    def dfs(cur, cost, start):
        nonlocal result

        if all(visited) and mat[cur][start] != 0:
            result = min(result, cost + mat[cur][start])
        if cost >= result:
            return

        for next in range(N):
            if not visited[next] and mat[cur][next] != 0:
                visited[next] = True
                dfs(next, cost + mat[cur][next], start)
                visited[next] = False

    for i in range(N):
        visited[i] = True
        dfs(i, 0, i)
        visited[i] = False

    print(result)


solution()