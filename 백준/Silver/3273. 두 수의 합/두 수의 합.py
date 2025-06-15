import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())


def solution():
    nums.sort()
    left = 0
    right = n - 1

    count = 0
    while left < right:
        acc = nums[left] + nums[right]
        
        if acc == x:
            count += 1
            left += 1
        elif acc > x:
            right -= 1
        elif acc < x:
            left += 1

    print(count)


solution()
