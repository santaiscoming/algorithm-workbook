import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def solution():
    result = sum(arr[0:m])
    prev = result
    left, right = 0, m

    while right < n:
        prev -= arr[left]
        prev += arr[right]

        if prev > result:
            result = prev

        left += 1
        right += 1

    print(result)


solution()
