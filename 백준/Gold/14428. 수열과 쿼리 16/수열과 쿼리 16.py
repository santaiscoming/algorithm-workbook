import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]


def solution():
    class SegTree:
        def __init__(self, data, op, ide) -> None:
            self.data = data
            self.k = self._getLeafSize()
            self.op = op
            self.ide = ide
            self.tree = [ide] * (self.k << 1)
            self._build()

        def _getLeafSize(self):
            i = 1
            while i < len(self.data):
                i <<= 1

            return i

        def _build(self):
            start = self.k
            self.tree[start : start + len(self.data)] = [*range(len(self.data))]

            for i in range(start - 1, 0, -1):
                self.tree[i] = self.op(
                    self.tree[i << 1], self.tree[i << 1 | 1], self.data
                )

        def update(self, i, v):
            self.data[i] = v
            self.tree[self.k + i] = i

            i += self.k
            i >>= 1
            while i:
                self.tree[i] = self.op(
                    self.tree[i << 1], self.tree[i << 1 | 1], self.data
                )
                i >>= 1

        def query(self, l, r):
            l = l + self.k
            r = r + self.k

            lr = self.ide
            rr = self.ide

            while l <= r:
                if l & 1:
                    lr = self.op(lr, self.tree[l], self.data)
                    l += 1
                if not r & 1:
                    rr = self.op(rr, self.tree[r], self.data)
                    r -= 1

                l >>= 1
                r >>= 1

            return self.op(lr, rr, self.data)

    def op(i, j, data):
        if any(idx >= len(data) for idx in [i, j]):
            return min(i, j, math.inf)

        v1 = data[i]
        v2 = data[j]

        if v1 == v2:
            return min(i, j)
        elif v1 > v2:
            return j
        else:
            return i

    segTree = SegTree(arr, op, math.inf)

    for command, a, b in queries:
        if command == 1:
            segTree.update(a - 1, b)
        if command == 2:
            print(segTree.query(a - 1, b - 1) + 1)


solution()
