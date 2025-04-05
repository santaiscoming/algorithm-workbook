import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, r, c = map(int, input().split())


def solution():
    def recur(n, r, c):
        if n == 0:
            return 0

        half = 1 << (n - 1)
        quadrant = 0

        if c >= half:
            quadrant += 1
        if r >= half:
            quadrant += 2

        offset = quadrant * (half * half)

        nr = r % half
        nc = c % half

        return offset + recur(n - 1, nr, nc)

    print(recur(n, r, c))


solution()
