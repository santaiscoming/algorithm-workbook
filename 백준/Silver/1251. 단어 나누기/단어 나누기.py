import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

s = input().rstrip()


def solution():
    n = len(s)

    words = []
    for i in range(1, n):
        for j in range(1, n - i):
            first = s[:i]
            second = s[i : i + j]
            third = s[i + j : n + 1]

            words.append(first[::-1] + second[::-1] + third[::-1])

    print(sorted(words)[0])


solution()
