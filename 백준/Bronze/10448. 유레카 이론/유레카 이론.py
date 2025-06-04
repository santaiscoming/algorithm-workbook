import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]


def solution():
    max_n = next(i for i in range(10000) if (i * (i + 1)) / 2 >= 1000)
    삼각수s = [int((j * (j + 1)) / 2) for j in range(1, max_n + 1)]

    def dfs(depth, s):
        if depth == 3:
            if s == 0:
                return True
        else:
            for i in 삼각수s:
                is삼각수 = dfs(depth + 1, s - i)
                if is삼각수:
                    return True

        return False

    for num in nums:
        if dfs(0, num):
            print(1)
        else:
            print(0)


solution()
