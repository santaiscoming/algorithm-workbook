import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())

googoo = [i + 1 for i in range(0, 9)]

list(map(lambda j: print(f"{N} * {j} = {j * N}"), googoo))
