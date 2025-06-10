import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution2():
    def dfs(i, aTeam, bTeam, aScore, bScore):
        nonlocal result
        
        if i == n:
            result = min(result, abs(aScore - bScore))
            return

        dfs(
            i + 1,
            aTeam + [i],
            bTeam,
            aScore + sum(mat[i][a] + mat[a][i] for a in aTeam),
            bScore,
        )
        dfs(
            i + 1,
            aTeam,
            bTeam + [i],
            aScore,
            bScore + sum(mat[i][b] + mat[b][i] for b in bTeam),
        )

    result = float("inf")
    dfs(1, [0], [], 0, 0)
    print(result)


solution2()


# 비트마스킹을 사용한다면 1 << (n - 1) - 1 로 범위를 잡아야함
# -> n번 밀고 -1해야 n개의 비트가 생김
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

    dfs(
        [0],  # 대칭성 제거를 위함
        [False] * n,
        1,
    )
    print(result)


# solution()
