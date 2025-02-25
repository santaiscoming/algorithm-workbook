import sys
import copy
from typing import List


# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]


def solution():
    def calc_mat(mat1, mat2):
        n = len(mat)
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                partial = 0
                for k in range(n):
                    partial += mat1[k][i] * mat2[j][k]

                result[j][i] = partial % 1000

        return result

    def power_calc(mat, b) -> List[List[int]]:
        if b <= 1:
            return [[mat[j][i] % 1000 for i in range(N)] for j in range(N)]

        if b % 2 == 0:
            half = power_calc(mat, b // 2)
            return calc_mat(half, half)
        else:
            return calc_mat(mat, power_calc(mat, b - 1))

    for arr in power_calc(mat, B):
        print(" ".join(map(str, arr)))


solution()
