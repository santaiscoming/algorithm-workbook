import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

tcs = [v for v in iter(lambda: input().rstrip(), ".")]


def solve():
    def getLPS(pat):
        n = len(pat)
        LPS = [0] * n
        length = 0

        for i in range(1, n):
            while pat[i] != pat[length] and length > 0:
                length = LPS[length - 1]

            if pat[i] == pat[length]:
                length += 1
                LPS[i] = length

        return LPS

    for tc in tcs:
        n = len(tc)
        lps = getLPS(tc)
        prefix = n - lps[-1]
        print(n // prefix) if n % prefix == 0 else print(1)


solve()
