import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T = int(input())
cases = [
    [int(input()), list(map(int, input().split())), int(input())] for _ in range(T)
]


def solution(cases):
    for case in cases:
        N, coins, target_money = case

        table = [[0] * (target_money + 1) for y in range(N + 1)]

        for y in range(1, N + 1):
            # 4원을 예시로 들었을때 0원을 만드는 경우는 4원을 쓰지않는 경우가 있으니까
            table[y][0] = 1
            cur_coin = coins[y - 1]

            for x in range(1, target_money + 1):
                # case 1 :본인보다 용량이 작은경우
                if cur_coin > x:
                    table[y][x] = table[y - 1][x]
                else:
                    # case 2 : 자기자신을 쓰는 경우의 수 + 자기자신을 전혀 안쓰는 경우의 수
                    table[y][x] = table[y][x - cur_coin] + table[y - 1][x]

        print(table[-1][-1])


solution(cases)
