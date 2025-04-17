import sys
from collections import deque

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
adj_mat = [list(map(int, input().split())) for _ in range(n)]


def bellan_soltion():
    dp = [[*r] for r in adj_mat]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] and dp[k][j]:
                    dp[i][j] = 1

    for r in dp:
        print(*r)


bellan_soltion()
