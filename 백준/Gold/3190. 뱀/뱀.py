import sys
from typing import Tuple, Deque
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]
L = int(input())
rotations = [
    [int(val) if idx == 0 else val for idx, val in enumerate(input().split())]
    for _ in range(L)
]


def solution():
    ms = 0
    q: Deque[Tuple[int, int]] = deque()
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_idx = 0
    q.append((0, 0))  # 대과리, popleft: 꼬리
    turn_idx = 0

    while True:
        head = q[len(q) - 1]
        cx, cy = head

        if not (0 <= cx < N and 0 <= cy < N):
            break

        dx, dy = dir[dir_idx]
        nx, ny = cx + dx, cy + dy

        q.append((nx, ny))
        ms += 1

        if q.count((nx, ny)) > 1:
            break

        if (ny, nx) in apples:
            apples.remove((ny, nx))
        else:
            q.popleft()

        if turn_idx < len(rotations):
            time, turn = rotations[turn_idx]
            if ms == time:
                if turn == "D":
                    dir_idx = (dir_idx + 1) % 4
                else:
                    dir_idx = (dir_idx - 1) % 4
                turn_idx += 1

    print(ms)


solution()
