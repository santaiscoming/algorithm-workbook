import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def solution(N, M, graph):
    direction = [(-1, -1), (-1, 0), (-1, 1)]

    memo: list[list[list[float, list[bool]]]] = [
        [[graph[y][x], [float("inf")] * 3] for x in range(M)] for y in range(N)
    ]

    for y in range(N):

        for x in range(M):
            if y == 0:
                for i in range(3):
                    # [[5, [5, 5, 5]], [8, [8, 8, 8]], [5, [5, 5, 5]], [1, [1, 1, 1]]]
                    # [[3 [inf, inf, inf], ...]
                    memo[y][x][1][i] = memo[y][x][0]
                continue

            for i, (dy, dx) in enumerate(direction):
                p_y, p_x = y + dy, x + dx

                if p_x < 0 or p_x >= M:
                    continue

                cur_check_fuel = memo[y][x][1][i]
                cur_spend_fuel = memo[y][x][0]

                for j, prev_spend_fuel in enumerate(memo[p_y][p_x][1]):

                    if i == j:
                        continue

                    memo[y][x][1][i] = min(
                        memo[y][x][1][i], cur_spend_fuel + prev_spend_fuel
                    )

    result = float("inf")
    for _, acc in memo[N - 1]:
        result = min(result, min(acc))

    print(result)


solution(N, M, graph)
