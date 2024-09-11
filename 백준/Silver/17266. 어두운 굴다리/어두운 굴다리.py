import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())  # 굴다리 길이
M = int(input())  # 가로등 개수
x = list(map(int, input().split()))


def solution(N, M, x):
    # 첫 번째 가로등과 굴다리 시작점 사이의 거리
    max_distance = x[0]

    # 가로등 사이의 최대 거리의 절반
    for i in range(1, M):
        max_distance = max(max_distance, (x[i] - x[i - 1]) / 2)

    # 마지막 가로등과 굴다리 끝점 사이의 거리
    max_distance = max(max_distance, N - x[-1])

    # 결과 출력
    print(math.ceil(max_distance))


solution(N, M, x)
