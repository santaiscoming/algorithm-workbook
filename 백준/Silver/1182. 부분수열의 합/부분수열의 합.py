import sys
from typing import List
from itertools import combinations
import bisect


# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, S = [int(x) for x in input().split()]
nums = list(map(int, input().split()))


def comb_solution():
    cnt = 0

    for i in range(1, N + 1):
        for comb in combinations(nums, i):
            if sum(comb) == S:
                cnt += 1

    print(cnt)


# comb_solution()


def subset_solution():
    cnt = 0

    def subset(arr: List[int], idx: int, target: int):
        nonlocal cnt
        print(f"arr : {arr}")
        print(f"arr2 : {arr[0:idx] + arr[idx : len(arr) - 1]}")

        if idx >= len(arr):
            return
        if target == sum(arr):
            cnt += 1
            return

        subset(arr[:idx] + arr[idx + 1 : len(arr)], idx + 1, target + arr[idx + 1])
        subset(arr[:idx] + arr[idx + 1 : len(arr)], idx + 1, target)

    def subsetSum1(A, S):
        print(A)

        nonlocal cnt
        # 기저 사례: S가 0이면 원하는 합을 달성했으므로 True
        if S == sum(A):
            cnt += 1
        # S가 음수이거나 A가 비어있으면 더 이상 진행할 수 없으므로 False
        elif S < 0 or not A:
            return
        else:
            # A에서 하나의 원소 z를 선택 (여기서는 리스트의 첫 번째 원소)
            z = A[0]
            # 원소 z를 포함한 경우와 포함하지 않은 경우를 재귀 호출하여 논리 OR 반환
            return subsetSum1(A[1:], S - z) or subsetSum1(A[1:], S)

    def subsetSumMeetInMiddle(nums, S):
        n = len(nums)
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]

        left_sums = []
        right_sums = []

        def genSums(arr, i, total, out):
            if i == len(arr):
                out.append(total)
                return
            # 현재 원소를 포함
            genSums(arr, i + 1, total + arr[i], out)
            # 포함하지 않음
            genSums(arr, i + 1, total, out)

        genSums(left, 0, 0, left_sums)
        genSums(right, 0, 0, right_sums)

        left_sums.sort()
        right_sums.sort()

        count = 0
        for x in left_sums:
            target = S - x
            # right_sums에서 target의 등장 횟수를 찾음
            l = bisect.bisect_left(right_sums, target)
            r = bisect.bisect_right(right_sums, target)
            count += r - l

        if S == 0:
            count -= 1  # 빈 부분집합 제거
        return count

    def subsetSum1_inplace(A, S):
        nonlocal cnt
        # 목표 합 S를 달성하면 True 반환
        if S == 0:
            cnt += 1
            return True
        # S가 음수이거나 A가 비어있으면 실패
        if S < 0 or not A:
            return False

        # 마지막 원소를 제거하여 선택 대상으로 만듭니다.
        z = A.pop()

        # z를 포함한 경우와 포함하지 않는 경우를 각각 탐색합니다.
        with_z = subsetSum1_inplace(A, S - z)
        without_z = subsetSum1_inplace(A, S)

        # 재귀 호출 후, 백트래킹: 원소를 다시 복원합니다.
        A.append(z)

        return with_z or without_z

    print(subsetSumMeetInMiddle(nums, S))
    # subsetSum1_inplace(nums, S)
    # print(cnt)


subset_solution()
