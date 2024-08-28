import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

N = int(input())


def solution(N):
    near_cnt = 1

    while True:
        if N <= 1:
            break

        N -= near_cnt * 6
        near_cnt += 1

    print(near_cnt)


solution(N)
