import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m)]


def solution():
    class MinMaxSegmentTree:
        def __init__(self, data) -> None:
            self.data = data
            self.k = self._getLeafSize()
            self.minTree = [math.inf] * (self.k << 1)
            self.maxTree = [-math.inf] * (self.k << 1)
            self._build()

        def _getLeafSize(self):
            return 1 << next(i for i in range(64) if 1 << i >= len(self.data))

        def _build(self):
            startIndex = self.k
            self.minTree[startIndex : startIndex + len(self.data)] = self.data
            self.maxTree[startIndex : startIndex + len(self.data)] = self.data

            for i in range(self.k - 1, 0, -1):
                self.minTree[i] = min(self.minTree[i << 1], self.minTree[i << 1 | 1])
                self.maxTree[i] = max(self.maxTree[i << 1], self.maxTree[i << 1 | 1])

        def query(self, l, r) -> tuple[int, int]:
            l += self.k
            r += self.k

            lResult = [math.inf, -math.inf]
            rResult = [math.inf, -math.inf]

            while l <= r:
                if l & 1:
                    lResult[0] = min(lResult[0], self.minTree[l])
                    lResult[1] = max(lResult[1], self.maxTree[l])
                    l += 1
                if not r & 1:
                    rResult[0] = min(rResult[0], self.minTree[r])
                    rResult[1] = max(rResult[1], self.maxTree[r])
                    r -= 1

                l >>= 1
                r >>= 1

            return (min(lResult[0], rResult[0]), max(lResult[1], rResult[1]))

    segmentTree = MinMaxSegmentTree(nums)
    [print(*segmentTree.query(a - 1, b - 1)) for a, b in commands]


solution()
