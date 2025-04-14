import sys
import heapq

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]


def solution():
    result = 0

    pq = [*cards]
    heapq.heapify(pq)

    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)

        temp = a + b
        result += temp
        heapq.heappush(pq, temp)

    print(result)


solution()
