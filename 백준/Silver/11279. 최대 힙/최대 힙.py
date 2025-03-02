from __future__ import annotations
import sys
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]


def solution():
    class Heap:
        def __init__(self) -> Heap:
            self.heap = []

        def getParentIdx(self, i):
            if i <= 0:
                return 0

            return (i - 1) // 2

        def getParent(self, i):
            return self.heap[self.getParentIdx(i)]

        def insert(self, num) -> None:
            self.heap.append(num)

            if len(self.heap) == 1:
                return 0

            self.bubbleUp()

        def bubbleUp(self):
            ci = len(self.heap) - 1
            pi = self.getParentIdx(ci)

            while ci != 0 and self.heap[pi] < self.heap[ci]:
                self.__swap(ci, pi)
                ci = pi
                pi = self.getParentIdx(ci)

        def __swap(self, i, j):
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        def extract(self) -> int:
            if len(self.heap) == 0:
                return 0
            if len(self.heap) == 1:
                return self.heap.pop()
            result = self.heap[0]
            self.heap[0] = self.heap.pop()

            def bubbleDown(start):
                parent = self.heap[start]
                l, r = (start * 2) + 1, (start * 2) + 2
                largest = None

                if l < len(self.heap) and self.heap[l] > parent:
                    largest = l

                if r < len(self.heap) and self.heap[r] > parent:
                    largest = r

                if largest is not None:
                    if largest != l:
                        largest = l if self.heap[l] > self.heap[r] else r

                    self.__swap(start, largest)
                    bubbleDown(largest)

            bubbleDown(0)

            return result

    heap = Heap()

    for num in nums:
        if num == 0:
            print(heap.extract())
        else:
            heap.insert(num)


solution()
