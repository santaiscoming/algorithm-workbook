import sys
from itertools import combinations
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution():
    def calcDist(x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

    bhcPositions = [(x, y) for y in range(n) for x in range(n) if mat[y][x] == 2]
    result = math.inf

    for bhcPositionCombi in combinations(bhcPositions, m):
        for x, y in bhcPositionCombi:
            mat[y][x] = 0

        currCombiTotalDist = 0
        
        for y in range(n):
            for x in range(n):
                if mat[y][x] == 1:
                    houseDist = math.inf
                    for bhcX, bhcY in bhcPositionCombi:
                        houseDist = min(houseDist, calcDist(x, y, bhcX, bhcY))

                    currCombiTotalDist += houseDist

        result = min(result, currCombiTotalDist)

        for x, y in bhcPositionCombi:
            mat[y][x] = 2

    print(result)


solution()
