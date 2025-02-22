import sys
from typing import Tuple

# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

# (M: 사대 수), (N: 동물 수), (L: 사정거리)
M, N, L = map(int, input().split())
shooter_pos = list(map(int, input().split()))
animal_pos = [list(map(int, input().split())) for _ in range(N)]


def solution():
    cnt = 0
    dead = []

    def get_distance(sx: int, aPos: Tuple[int, int]):
        (ax, ay) = aPos
        return abs(sx - ax) + ay

    for s_x in shooter_pos:
        for aPos in animal_pos:
            if aPos in dead:
                continue
            if L >= get_distance(s_x, aPos):
                cnt += 1
                dead.append(aPos)

    print(cnt)


solution()
