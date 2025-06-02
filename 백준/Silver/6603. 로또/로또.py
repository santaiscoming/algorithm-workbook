import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

tcs = [list(map(int, line.split())) for line in iter(lambda: input().rstrip(), "0")]


def solution():
    def dfs(n, nums, lottery, visited, depth, j):
        if depth == 6:
            print(*lottery)
            return

        for i in range(j, n):
            if not visited[i]:
                lottery.append(nums[i])
                visited[i] = True
                dfs(n, nums, lottery, visited, depth + 1, i + 1)
                visited[i] = False
                lottery.pop()

    for i, v in enumerate(tcs):
        n, *rest = v
        dfs(n, rest, [], [False] * n, 0, 0)
        print("") if i != len(tcs) - 1 else None


solution()
