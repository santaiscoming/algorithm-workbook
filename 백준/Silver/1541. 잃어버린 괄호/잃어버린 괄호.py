import sys
from functools import reduce

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

exp = input().rstrip()


def solution(exp):
    split_exp = exp.split("-")

    result = 0

    for i, exp in enumerate(split_exp):
        cur_exp = reduce(lambda acc, cur: acc + cur, list(map(int, exp.split("+"))))
        # 시작값은 더해주고 시작한다
        if i == 0:
            result += cur_exp
            continue

        result -= cur_exp

    print(result)


solution(exp)
