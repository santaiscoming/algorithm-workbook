import sys
from bisect import bisect_left


# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


def binary_solution():
    result = []

    for num in nums:
        if not result:
            result.append(num)
        else:
            idx = bisect_left(result, num)
            if idx == len(result):
                result.append(num)
            else:
                result[idx] = num

    print(len(result))


binary_solution()


def solution():
    dp = [1] * n  # 각 위치에서 끝나는 LIS의 길이

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:  # 증가하는 수열 조건 확인
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


# solution()
