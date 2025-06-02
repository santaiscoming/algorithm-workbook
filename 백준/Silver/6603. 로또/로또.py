import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

tcs = [list(map(int, line.split())) for line in iter(lambda: input().rstrip(), "0")]

# 조합일땐 visited 필요
# 순열일땐 불필요 start가 이미 제외


def solution():
    def dfs(nums, lottery, depth, start):
        if depth == 6:
            print(*lottery)
            return

        for i in range(start, len(nums)):
            lottery.append(nums[i])
            dfs(nums, lottery, depth + 1, i + 1)
            lottery.pop()

    for i, v in enumerate(tcs):
        _, *rest = v
        dfs(rest, [], 0, 0)
        print("") if i != len(tcs) - 1 else None


solution()
