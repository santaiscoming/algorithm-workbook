import sys

# sys.stdin = open("./input.txt", "r")


def readlines(count=1):
    return [input() for _ in range(count)]


N, nums, M, check_nums = readlines(4)
nums = list(map(int, nums.split()))
nums.sort()
check_nums = list(map(int, check_nums.split()))


# 종료조건 :
# 1. 키가 일치하는 경우
# 2. 검색범위가 더이상 없는경우

# key > center : {center + 1} ~ {last}
# start = {center + 1}
# key < center : {start} ~ {center - 1}
# last = {center - 1}


def divide_search(nums, check_num):
    start = 0
    last = len(nums) - 1

    while True:
        center = (start + last) // 2

        # find key
        if nums[center] == check_num:
            return 1
        # not found
        if start > last:
            return 0
        # key < center
        if nums[center] < check_num:
            start = center + 1
            continue
        # key > center
        if nums[center] > check_num:
            last = center - 1
            continue


def solution(N, nums, M, check_nums):
    [print((divide_search(nums, check_num))) for check_num in check_nums]


solution(N, nums, M, check_nums)
