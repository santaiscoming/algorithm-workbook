import sys
from typing import Tuple, List
import math

# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

# (M: 사대 수), (N: 동물 수), (L: 사정거리)
M, N, L = map(int, input().split())
shooters: List[int] = list(map(int, input().split()))
animals: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


def get_distance(sx: int, aPos: Tuple[int, int]) -> int:
    (ax, ay) = aPos
    return abs(sx - ax) + ay


def binary_search(arr: List[int], target, left, right):
    if left >= right:
        return left

    mid = (left + right) // 2

    if arr[mid] > target:
        return binary_search(arr, target, left, mid)
    else:
        return binary_search(arr, target, mid + 1, right)


def solution():
    shooters.sort()

    cnt = 0

    for aPos in animals:
        ax, ay = aPos
        idx = binary_search(shooters, ax, 0, len(shooters) - 1)

        dist = math.inf
        if idx < len(shooters):
            dist = min(dist, get_distance(shooters[idx], aPos))
        if idx - 1 >= 0:
            dist = min(dist, get_distance(shooters[idx - 1], aPos))
        if dist <= L:
            cnt += 1

    print(cnt)


solution()
