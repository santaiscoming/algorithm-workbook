import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution():
    INF = float("inf")
    pre_mat = [[mat[y][x] + mat[x][y] for x in range(n)] for y in range(n)]
    result = INF

    def calc(picekd):
        a_team = picekd
        b_team = [i for i in range(n) if i not in a_team]

        a_score = 0
        b_score = 0
        for i in range(len(a_team)):
            for j in range(i, len(a_team)):
                a_score += pre_mat[a_team[i]][a_team[j]]

        for i in range(len(b_team)):
            for j in range(i, len(b_team)):
                b_score += pre_mat[b_team[i]][b_team[j]]

        return abs(a_score - b_score)

    def dfs(picked, visited, start_idx):
        nonlocal result

        if 0 < len(picked) < n:
            result = min(result, calc(picked))

        for i in range(start_idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(picked + [i], visited, i)
                visited[i] = False

    dfs([0], [False] * n, 1)
    print(result)


solution()
