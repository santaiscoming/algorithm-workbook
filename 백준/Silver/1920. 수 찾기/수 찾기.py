import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
nums_1 = [int(num) for num in input().split()]
M = int(input())
nums_2 = [int(num) for num in input().split()]


def binary_search(arr, find_val):
    # center값이 find_val보다 큰지 작은지 확인
    left = 0
    right = N - 1
    center = None

    while True:
        center = (right + left) // 2

        if arr[center] == find_val:
            print(1)
            break

        if arr[center] < find_val:
            left = center + 1
        elif arr[center] > find_val:
            right = center - 1

        # 종료조건:
        if left > right:
            print(0)
            break


def solve(arr, arr2):
    arr.sort()

    for num in arr2:
        binary_search(arr, num)

        # 입력


solve(nums_1, nums_2)

# set 자료구조에 in을 활용할수도 있다.
# N = int(input())
# set_nums = set(map(int, input().split()))
# M = int(input())
# numbers = list(map(int, input().split()))

# for num in numbers:
#     print(1) if num in set_nums else print(0)
