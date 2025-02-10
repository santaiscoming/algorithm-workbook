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

    # cur : next
    # start : for 되돌아가는 비용
    def dfs(cur, start, cost):
        nonlocal result

        if cost >= result:
            return

        # mat[cur][start] -> 다시 되돌아가는 비용
        if all(visited) and mat[cur][start] != 0:
            result = min(result, cost + mat[cur][start])
            return

        for next in range(N):
            if not visited[next] and mat[cur][next] != 0:
                visited[next] = True
                dfs(next, start, cost + mat[cur][next])
                visited[next] = False

    for i in range(N):
        visited[i] = True
        dfs(i, i, 0)
        visited[i] = False

    print(result)


solution()