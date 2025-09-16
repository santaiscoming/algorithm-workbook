import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n, m = list(map(int, input().split()))
nums = [int(input()) for _ in range(n)]
pairs = [list(map(int, input().split())) for _ in range(m)]


def solve():
    class SegmentTree:
        def __init__(self, data):
            self.data = data
            self.n = len(data)
            self.k = self.getLeafSize()
            self.tree = [math.inf] * (self.k << 1)
            self.build()

        def getLeafSize(self):
            k = 1

            while k < self.n:
                k <<= 1

            return k

        def build(self):
            self.tree[self.k : self.k + self.n] = [*self.data]

            for i in range(self.k - 1, 0, -1):
                left = self.tree[i << 1]
                right = self.tree[i << 1 | 1]

                self.tree[i] = min(left, right)

        def query(self, start, end):
            resL, resR = math.inf, math.inf
            l, r = start + self.k, end + self.k

            while l <= r:
                if l & 1:
                    resL = min(resL, self.tree[l])
                    l += 1
                if not r & 1:
                    resR = min(resR, self.tree[r])
                    r -= 1

                l >>= 1
                r >>= 1

            return min(resL, resR)

    segmentTree = SegmentTree(nums)
    for query in pairs:
        start, end = query
        print(segmentTree.query(start - 1, end - 1))


solve()
