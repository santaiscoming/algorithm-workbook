import sys
import heapq
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())


def solution():
    MAX_SIZE = 100001
    dist = [math.inf] * MAX_SIZE
    dist[n] = 0

    pq = []
    heapq.heappush(pq, (0, n))

    while pq:
        time, pos = heapq.heappop(pq)

        if dist[pos] < time:
            continue

        if pos == k:
            print(time)
            return

        if pos * 2 < MAX_SIZE and dist[pos * 2] > time:
            dist[pos * 2] = time
            heapq.heappush(pq, (time, pos * 2))

        if pos - 1 >= 0 and dist[pos - 1] > time + 1:
            dist[pos - 1] = time + 1
            heapq.heappush(pq, (time + 1, pos - 1))

        if pos + 1 < MAX_SIZE and dist[pos + 1] > time + 1:
            dist[pos + 1] = time + 1
            heapq.heappush(pq, (time + 1, pos + 1))


solution()
