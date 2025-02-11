import sys
import math

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, M = [int(i) for i in input().split()]
trees = [int(tree) for tree in input().split()]


def solution(N, M, trees):
    result = 0
    pl, pr = 0, max(trees)

    while True:
        if pl > pr:
            break

        pc = (pl + pr) // 2
        cutted_height = get_cutted_height(trees, pc)

        if cutted_height >= M:
            result = pc
            pl = pc + 1
        else:
            pr = pc - 1

    print(result)


def get_cutted_height(trees, height):
    result = 0

    for tree in trees:
        if tree <= height:
            continue

        cutted = tree - height
        result += cutted

    return result


solution(N, M, trees)
