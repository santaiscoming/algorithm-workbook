import sys
from collections import deque
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

m, n = map(int, input().split())
mat = [list(map(int, input().rstrip())) for _ in range(n)]


def solution():
    destroy_mat = [[math.inf] * m for _ in range(n)]
    result = math.inf

    q = deque()
    q.append((0, 0, 0))
    destroy_mat[0][0] = 0

    while q:
        x, y, destroy = q.popleft()

        if (x, y) == (m - 1, n - 1):
            result = min(result, destroy)

        for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if destroy_mat[ny][nx] > destroy + 1 and mat[ny][nx] == 1:
                    destroy_mat[ny][nx] = destroy + 1
                    q.append((nx, ny, destroy + 1))
                if destroy_mat[ny][nx] > destroy and mat[ny][nx] == 0:
                    destroy_mat[ny][nx] = destroy
                    q.appendleft((nx, ny, destroy))

    print(destroy_mat[-1][-1])


solution()
