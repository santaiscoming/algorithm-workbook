import sys
import math
from operator import add

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m + k)]


def solution():
    class SegmentTree:
        def __init__(self, data, op, ide) -> None:
            self.data = data
            self.op = op
            self.ide = ide
            self.k = self.getLeafCount()
            self.tree = self._init(self.k, data)

        def _init(self, n, data):
            tree = [0] * (n << 1)
            tree[n : n + len(data)] = data

            for i in range(self.k - 1, 0, -1):
                tree[i] = self.op(tree[i << 1], tree[i << 1 | 1])

            return tree

        def getLeafCount(self):
            i = 1

            while i < len(self.data):
                i <<= 1

            return i

        def updata(self, i, v):
            i += self.k
            self.tree[i] = v

            i >>= 1
            while i > 0:
                self.tree[i] = self.op(self.tree[i << 1], self.tree[i << 1 | 1])
                i >>= 1

        def query(self, l, r):
            l += self.k
            r += self.k

            lResult = self.ide
            rResult = self.ide

            while l <= r and r >= 0:
                if l & 1:
                    lResult = self.op(lResult, self.tree[l])
                    l += 1
                if not (r & 1):
                    rResult = self.op(rResult, self.tree[r])
                    r -= 1

                l >>= 1
                r >>= 1

            return self.op(lResult, rResult)

    segmentTree = SegmentTree(nums, add, 0)

    for op, b, c in commands:
        if op == 1:
            segmentTree.updata(b - 1, c)
        if op == 2:
            print(segmentTree.query(b - 1, c - 1))


solution()
