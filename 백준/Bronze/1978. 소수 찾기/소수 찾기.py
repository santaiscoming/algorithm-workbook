import sys
import math

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

global N
global nums

N = int(input())
nums = [int(num) for num in input().split(" ")]


def is_sosu(num):
    if num == 1:
        return False

    limit = math.floor(math.sqrt(num)) + 1
    for i in range(2, limit):
        if num % i == 0:
            return False

    return True


def solution():
    result = []

    for num in nums:
        result.append(is_sosu(num))

    return len(list(filter(lambda bool: bool, result)))


print(solution())
