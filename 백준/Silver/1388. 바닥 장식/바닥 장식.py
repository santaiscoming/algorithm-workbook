import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, M = map(int, input().split())

floor = [list(input().rstrip()) for _ in range(N)]

# 백준 1388

# - 와 | 로 이루어진 이차원배열
# 1. 두개의 - 가 인접하고 같은 행에 있다면 같은 나무판자
# 2. 두개의 | 가 인접하고 같은 열에 있다면 같은 나무판자
# 바닥을 장식하는데 필요한 나무판자 개수를 구하라

# 6 9
# -||--||--
# --||--||-
# |--||--||
# ||--||--|
# -||--||--
# --||--||-
# answer = 31


def solution(floor, N, M):

    result = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                result += 1
                if floor[i][j] == "-":
                    for k in range(j, M):
                        if floor[i][k] == "-":
                            visited[i][k] = True
                        else:
                            break
                else:
                    for k in range(i, N):
                        if floor[k][j] == "|":
                            visited[k][j] = True
                        else:
                            break

    print(result)


solution(floor, N, M)
