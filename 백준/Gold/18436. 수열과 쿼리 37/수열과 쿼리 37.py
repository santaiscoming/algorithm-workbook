import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]


def solution():
    class SegTree:
        def __init__(self, data, isOddEvenFunc) -> None:
            self.data = data
            self.isOddEvenFunc = isOddEvenFunc
            self.k = self._getLeafSize()
            self.tree = [0] * (self.k << 1)
            self._init()

        def _getLeafSize(self):
            i = 1
            while i < len(self.data):
                i <<= 1

            return i

        def _init(self):
            for i in range(len(self.data)):
                j = i + self.k
                self.tree[j] = 1 if self.isOddEvenFunc(self.data[i]) else 0

            i = self.k
            while i:
                i -= 1
                self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

        def query(self, start, end):
            l, r = start + self.k, end + self.k

            lr, rr = 0, 0

            while l <= r:
                if l & 1:
                    lr += self.tree[l]
                    l += 1
                if not r & 1:
                    rr += self.tree[r]
                    r -= 1

                l >>= 1
                r >>= 1

            return lr + rr

        def update(self, i, v):
            i += self.k
            self.tree[i] = 1 if self.isOddEvenFunc(v) else 0

            while i:
                i >>= 1
                self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    evenSegTree = SegTree(nums, lambda x: True if x % 2 == 0 else False)
    oddSegTree = SegTree(nums, lambda x: True if x % 2 == 1 else False)

    for op, l, r in queries:
        if op == 1:
            evenSegTree.update(l - 1, r)
            oddSegTree.update(l - 1, r)
        if op == 2:
            print(evenSegTree.query(l - 1, r - 1))
        if op == 3:
            print(oddSegTree.query(l - 1, r - 1))


solution()
