import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]


def solution(numbers, N):
    ascending_numbers = sorted(numbers)

    for num in ascending_numbers:
        print(num)


solution(numbers, N)
