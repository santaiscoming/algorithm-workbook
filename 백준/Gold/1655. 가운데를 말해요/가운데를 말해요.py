import sys
import heapq

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]


def solution():
    minH = []
    maxH = []

    for num in nums:

        if not maxH or num <= -maxH[0]:
            heapq.heappush(maxH, -num)
        else:
            heapq.heappush(minH, num)

        if len(maxH) > len(minH) + 1:
            heapq.heappush(minH, -heapq.heappop(maxH))
        elif len(maxH) < len(minH):
            heapq.heappush(maxH, -heapq.heappop(minH))

        print(-maxH[0])


solution()
