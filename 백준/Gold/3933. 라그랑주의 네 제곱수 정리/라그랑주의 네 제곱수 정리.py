import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


nums = [n for n in iter(lambda: int(input()), 0)]


def solution_recursive():
    MAX_N = 2**15
    dp = [0] * (MAX_N + 1)
    squares = [i * i for i in range(1, int(math.sqrt(MAX_N)) + 1)]

    def generate_sums(k_target, current_sum, start_idx):
        # k_target: 만들고자 하는 제곱수 합의 개수 (1, 2, 3, 4)
        # current_sum: 현재까지 만들어진 합
        # start_idx: 제곱수 배열에서 탐색을 시작할 인덱스 (i<=j<=k.. 조건 충족)

        # 목표 개수에 도달하지 않았어도, 중간 합들을 모두 기록
        # (예: 2개 합을 만드는 과정에서 나온 1개 합도 유효)
        if current_sum > 0:
            dp[current_sum] += 1

        if k_target == 4:
            return

        for i in range(start_idx, len(squares)):
            next_sum = current_sum + squares[i]
            if next_sum > MAX_N:
                break
            generate_sums(k_target + 1, next_sum, i)

    generate_sums(0, 0, 0)

    for num in nums:
        print(dp[num])


solution_recursive()
