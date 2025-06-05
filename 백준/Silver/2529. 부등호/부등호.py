import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
brackets = input().rstrip().split(" ")


def solution():
    visited = [False] * 10
    result = []

    def dfs(depth, num):
        nonlocal result

        if depth == n:
            result.append(num)
            return

        for i in range(10):
            if not visited[i] and eval(f"{num[-1]}{brackets[depth]}{i}"):
                visited[i] = True
                dfs(depth + 1, num + str(i))
                visited[i] = False

    for i in range(10):
        visited[i] = True
        dfs(0, str(i))
        visited[i] = False

    print(max(result))
    print(min(result))


solution()
