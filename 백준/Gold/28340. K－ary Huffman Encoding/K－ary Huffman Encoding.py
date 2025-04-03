import sys
from typing import List
import heapq

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())
cases = []
for _ in range(t):
    n, k = map(int, input().split())
    freqs = list(map(int, input().split()))
    cases.append((n, k, freqs))


def solution():
    def huffman(n: int, k: int, freqs: List[int]):
        dummy_node_cnt = (k - 1 - (n - 1) % (k - 1)) % (k - 1)

        for _ in range(dummy_node_cnt):
            freqs.append(0)

        heapq.heapify(freqs)

        total_cost = 0

        while len(freqs) > 1:
            acc = 0
            for _ in range(k):
                acc += heapq.heappop(freqs)

            total_cost += acc
            heapq.heappush(freqs, acc)

        return total_cost

    for case in cases:
        n, k, freqs = case

        print(huffman(n, k, freqs))


solution()
