import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

s = input().rstrip()


def solution():
    n = len(s)

    words = []
    for i in range(1, n):
        first = s[:i]
        for j in range(1, n):
            second = s[i : i + j]
            if len(second) < 1:
                continue
            for k in range(1, n):
                third = s[i + j : max(i + j + k, n)]
                if len(third) < 1:
                    continue

                words.append(first[::-1] + second[::-1] + third[::-1])

    print(sorted(words)[0])


solution()
