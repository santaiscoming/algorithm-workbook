import sys
import heapq

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T = int(input())
cases = []
for _ in range(T):
    M = int(input())
    nums = []
    for _ in range(M // 10 + 1):
        nums.extend(list(map(int, input().split())))
    cases.append((M, nums))


def solution():
    for case in cases:
        M, nums = case
        cnt = (M // 2) - 1 if M % 2 == 0 else (M // 2) + 1
        result = []

        lH = []
        rH = []

        for idx, num in enumerate(nums):
            if not lH or num <= -lH[0]:
                heapq.heappush(lH, -num)
            else:
                heapq.heappush(rH, num)

            if len(rH) > len(lH):
                heapq.heappush(lH, -heapq.heappop(rH))
            elif len(lH) > len(rH) + 1:
                heapq.heappush(rH, -heapq.heappop(lH))

            if (idx + 1) % 2 == 1:
                result.append(-lH[0])

        print(cnt)
        for i in range(0, len(result), 10):
            print(*result[i : i + 10])


solution()
