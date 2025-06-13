import sys
from itertools import combinations

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())


def solution():
    [print(*combi) for combi in combinations(range(1, n + 1), m)]


solution()


def solution2():
    def dfs(numStr, picked, start, visited):
        if picked == m:
            print(*list(numStr))
            return

        for i in range(start, n + 1):
            if not visited[i]:
                visited[i] = True
                dfs(numStr + str(i), picked + 1, i + 1, visited)
                visited[i] = False

    dfs("", 0, 1, [False] * (n + 1))
    print("")


# solution2()
