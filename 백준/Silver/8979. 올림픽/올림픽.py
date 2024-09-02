# https://www.acmicpc.net/problem/8979

import sys
from typing import List

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def comp(x, y):
    if x > y:
        return x > y
    else:
        return x < y


def solution(N, K, arr: List):
    arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    find_country_idx = [countryNum for countryNum, _, _, _ in arr].index(K)

    for i, (country_num, gold, silver, bronze) in enumerate(arr):
        cmp_country = arr[i]

        if arr[find_country_idx][1:] == cmp_country[1:]:
            print(i + 1)
            break


solution(N, K, arr)
