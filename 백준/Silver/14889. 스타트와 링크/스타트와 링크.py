import sys
from itertools import combinations

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
INF = float("inf")


def recur_solution():
    new_mat = [[mat[i][j] + mat[j][i] for i in range(n)] for j in range(n)]

    def calc(picked):
        a_team = picked
        b_team = [i for i in range(n) if i not in a_team]

        a_score = 0
        b_score = 0

        for i in range(n // 2):
            for j in range(i, n // 2):
                a_score += new_mat[a_team[i]][a_team[j]]
                b_score += new_mat[b_team[i]][b_team[j]]

        return abs(a_score - b_score)

    def dfs(picked, start_idx, visited):
        nonlocal result

        if len(picked) == n // 2:
            result = min(result, calc(picked))

        for i in range(start_idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(picked + [i], i, visited)
                visited[i] = False

    result = INF
    dfs([], 0, [False] * n)
    print(result)


recur_solution()


def combi_solution():
    def calc(a_team, b_team):
        a_score = 0
        b_score = 0

        for i in range(n // 2):
            for j in range(i, n // 2):
                a_score += mat[a_team[i]][a_team[j]]
                a_score += mat[a_team[j]][a_team[i]]
                b_score += mat[b_team[i]][b_team[j]]
                b_score += mat[b_team[j]][b_team[i]]

        return abs(a_score - b_score)

    result = INF

    for combi in combinations(range(n), n // 2):
        a_team = list(combi)
        b_team = [i for i in range(n) if i not in a_team]

        result = min(result, calc(a_team, b_team))

    print(result)


# combi_solution()


def solution():
    def calc(a_team, b_team):
        a_score = 0
        b_score = 0
        for i in range(n // 2):
            for j in range(n // 2):
                a_score += mat[a_team[i]][a_team[j]]
                a_score += mat[a_team[j]][a_team[i]]

                b_score += mat[b_team[i]][b_team[j]]
                b_score += mat[b_team[j]][b_team[i]]

        return abs(a_score - b_score)

    def dfs(a_team, b_team, visited, start):
        nonlocal result

        if len(a_team) + len(b_team) == n:
            result = min(result, calc(a_team, b_team))

        if len(a_team) < n // 2:
            for i in range(start, n):
                if not visited[i]:
                    visited[i] = True
                    dfs(a_team + [i], b_team, visited, start + 1)
                    visited[i] = False

        if len(b_team) < n // 2:
            for i in range(start, n):
                if not visited[i]:
                    visited[i] = True
                    dfs(a_team, b_team + [i], visited, start + 1)
                    visited[i] = False

    result = INF
    dfs([], [], [False] * n, 0)
    print(result)


# solution()
