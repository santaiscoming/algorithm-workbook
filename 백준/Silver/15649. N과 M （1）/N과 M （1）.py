import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())


def solution():
    def dfs(numStr, depth, visited):
        if depth == m:
            print(*list(numStr))
            return

        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = True
                dfs(numStr + str(i), depth + 1, visited)
                visited[i] = False

    dfs("", 0, [False] * (n + 1))


solution()
