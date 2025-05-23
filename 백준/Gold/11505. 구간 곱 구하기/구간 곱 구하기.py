import sys
from operator import mul
from typing import Callable

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m + k)]


def solution():
    DIVISOR = 1000000007

    class SegmentTree:
        def __init__(
            self, data: list[int], op: Callable[[int, int], int], ide: int
        ) -> None:
            self.data = data
            self.op = op
            self.ide = ide
            self.k = self._getLeafSize()
            self.tree = [self.ide] * (self.k << 1)
            self._build()

        def _getLeafSize(self):
            return 1 << next(i for i in range(64) if (1 << i) >= len(self.data))

        def _build(self):
            startIdx = self.k
            self.tree[startIdx : startIdx + len(self.data)] = self.data

            for i in range(self.k - 1, 0, -1):
                self.tree[i] = (
                    self.op(self.tree[i << 1], self.tree[i << 1 | 1]) % DIVISOR
                )

        def update(self, i, v):
            i += self.k
            self.tree[i] = v

            i >>= 1
            while i:
                self.tree[i] = (
                    self.op(self.tree[i << 1], self.tree[i << 1 | 1]) % DIVISOR
                )
                i >>= 1

        def query(self, l, r):
            l += self.k
            r += self.k

            lResult = self.ide
            rResult = self.ide

            while l <= r:
                if l & 1:
                    lResult = self.op(lResult, self.tree[l]) % DIVISOR
                    l += 1
                if not r & 1:
                    rResult = self.op(rResult, self.tree[r]) % DIVISOR
                    r -= 1

                l >>= 1
                r >>= 1

            return self.op(lResult, rResult) % DIVISOR

    segmentTree = SegmentTree(nums, mul, 1)

    for op, b, c in commands:
        if op == 1:
            segmentTree.update(b - 1, c)
        elif op == 2:
            print(segmentTree.query(b - 1, c - 1))


solution()
