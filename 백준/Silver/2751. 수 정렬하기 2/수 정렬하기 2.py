import sys
import random

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]


def solution():
    def quickSort(left, right):
        if left >= right:
            return

        pi = partition(left, right)

        quickSort(left, pi - 1)
        quickSort(pi, right)

    def partition(left: int, right: int):
        pi = random.randint(left, right)
        p = nums[pi]
        pl, pr = left, right

        while pl <= pr:
            while nums[pl] < p:
                pl += 1
            while nums[pr] > p:
                pr -= 1

            if pl <= pr:
                swap(nums, pl, pr)
                pl += 1
                pr -= 1

        return pl

    quickSort(0, len(nums) - 1)
    [print(num) for num in nums]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


solution()
