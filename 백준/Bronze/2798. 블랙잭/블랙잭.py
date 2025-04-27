import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))


def solution():
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                acc = sum([cards[i], cards[j], cards[k]])
                result = max(result, acc) if acc <= m else result

    print(result)


solution()
