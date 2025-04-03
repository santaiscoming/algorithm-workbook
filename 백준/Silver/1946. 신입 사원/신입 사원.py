import sys
import math


# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    person = [list(map(int, input().split())) for _ in range(n)]
    cases.append((n, person))


def solution():
    # 귀류법으로 현재 알고리즘의 합격자가 예제 2번 기준으로 3명일때
    # 3명보다 많은 지원자가 있음을 가정하고
    # 마지막 합격자보다 더 나은 순위가 없을(모순)을 확인하면 된다
    def max_in_cnt(n, people):
        people.sort(key=lambda x: x[0])
        min_rate = math.inf

        return sum(
            1 for ranks in people if min_rate > ranks[1] and (min_rate := ranks[1])
        )

    for n, people in cases:
        print(max_in_cnt(n, people))


solution()
