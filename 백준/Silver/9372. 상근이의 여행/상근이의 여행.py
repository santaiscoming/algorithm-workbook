import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline


t = int(input())
tcs = [
    (
        (nm := input().split()),
        (n := int(nm[0])),
        (m := int(nm[1])),
        [list(map(int, input().split())) for _ in range(m)],
    )[1:4]
    for _ in range(t)
]


def solution():
    for n, _, _ in tcs:
        print(n - 1)


solution()
