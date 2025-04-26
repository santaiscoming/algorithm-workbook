import sys
from collections import deque
import copy
from itertools import combinations

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution():
    def infect(mat, virusPos):
        q = deque([*virusPos])
        visited = [[False] * m for _ in range(n)]

        while q:
            x, y = q.popleft()

            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and not visited[ny][nx]
                    and mat[ny][nx] == 0
                ):
                    visited[ny][nx] = True
                    mat[ny][nx] = 2
                    q.append((nx, ny))

        return mat

    def getSaftyPoses(mat):
        return [(x, y) for x in range(m) for y in range(n) if mat[y][x] == 0]

    def getSafetyCount(mat):
        return len(getSaftyPoses(mat))

    def getVirusPoses(mat):
        return [(x, y) for x in range(m) for y in range(n) if mat[y][x] == 2]

    result = 0
    safetyAreas = getSaftyPoses(mat)
    virusPoses = getVirusPoses(mat)

    for walls in combinations(safetyAreas, 3):
        w1, w2, w3 = walls

        newMat = copy.deepcopy(mat)
        newMat[w1[1]][w1[0]] = 1
        newMat[w2[1]][w2[0]] = 1
        newMat[w3[1]][w3[0]] = 1

        infect(newMat, virusPoses)
        safetyCount = getSafetyCount(newMat)
        result = max(result, safetyCount)

        newMat[w1[1]][w1[0]] = 1
        newMat[w2[1]][w2[0]] = 1
        newMat[w3[1]][w3[0]] = 1

    print(result)


solution()
