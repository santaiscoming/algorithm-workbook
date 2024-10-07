import sys
import math


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

global T, nums

T = int(input())
nums = [int(input()) for i in range(T)]

import sys


def sieve(max_num):
    # """에라토스테네스의 체를 이용해 소수를 미리 구함."""
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return is_prime


def find_goldbach_pair(num, is_prime):
    # """주어진 숫자 num에 대해 골드바흐 파티션을 찾음."""
    for i in range(num // 2, 1, -1):
        if is_prime[i] and is_prime[num - i]:
            return i, num - i
    return None


def solution():
    max_num = max(nums)
    is_prime = sieve(max_num)

    results = []
    for num in nums:
        a, b = find_goldbach_pair(num, is_prime)
        results.append(f"{a} {b}")

    print("\n".join(results))


solution()
