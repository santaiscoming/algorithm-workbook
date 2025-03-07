import sys
import heapq

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
axis = [tuple(map(int, input().split())) for _ in range(n)]
d = int(input())


def solution():
    global axis

    axis = [sorted(x) for x in axis if abs(x[1] - x[0]) <= d]
    axis.sort(key=lambda x: x[1])

    result = 0
    h = []

    for l, r in axis:
        # 시작점을 넣을것
        heapq.heappush(h, l)

        while True:
            if not h:
                break

            startTrack = r - d
            minStartHomeOrOffice = h[0]

            if minStartHomeOrOffice < startTrack:
                heapq.heappop(h)
                continue

            break

        result = max(result, len(h))

    print(result)


solution()
