import sys
from functools import reduce

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

N = int(input())
weights = [int(input()) for _ in range(N)]

# 작은수로 정렬한다


def solution(N, weights):
    max_weight = 0
    copied_weights = sorted(weights)

    for i in range(N):
        cur_acc = copied_weights[i] * (N - i)
        max_weight = max(max_weight, cur_acc)

    return max_weight


print(solution(N, weights))
