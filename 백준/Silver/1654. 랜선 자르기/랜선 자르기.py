import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]


def solution():
    def getCuttedLan(arr, l):
        return sum(v // l for v in arr)

    left, right = 1, max(arr)
    result = 0

    while left <= right:
        mid = (right + left) // 2
        count = getCuttedLan(arr, mid)

        if count >= k:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)


solution()
