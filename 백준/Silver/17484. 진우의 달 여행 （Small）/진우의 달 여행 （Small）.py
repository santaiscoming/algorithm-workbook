import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def solution(N, M, graph):
    dp = [[[float("inf")] * 3 for _ in range(M)] for _ in range(N)]

    for x in range(M):
        dp[0][x][0] = graph[0][x]
        dp[0][x][1] = graph[0][x]
        dp[0][x][2] = graph[0][x]

    for y in range(1, N):
        for x in range(M):
            if x >= 1:
                dp[y][x][0] = graph[y][x] + min(
                    dp[y - 1][x - 1][1], dp[y - 1][x - 1][2]
                )
            if x < M - 1:
                dp[y][x][2] = graph[y][x] + min(
                    dp[y - 1][x + 1][0], dp[y - 1][x + 1][1]
                )

            dp[y][x][1] = graph[y][x] + min(dp[y - 1][x][0], dp[y - 1][x][2])

    result = float("inf")
    for x in range(M):
        result = min(result, dp[N - 1][x][0], dp[N - 1][x][1], dp[N - 1][x][2])

    print(result)


solution(N, M, graph)
