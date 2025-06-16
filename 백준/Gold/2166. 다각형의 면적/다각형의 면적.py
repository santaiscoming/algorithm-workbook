import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
axis = [list(map(int, input().split())) for _ in range(n)]


def solution():
    result = 0

    for i in range(n):
        x1, y1 = axis[i]
        x2, y2 = axis[(i + 1) % n]

        result += x1 * y2
        result -= x2 * y1

    print(f"{abs(result) / 2:.1f}")


solution()
