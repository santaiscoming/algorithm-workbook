import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

nums = [int(input().rstrip()) for _ in range(9)]

max = max(nums)
idx = nums.index(max) + 1

print(max)
print(idx)
