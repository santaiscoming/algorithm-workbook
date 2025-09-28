import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())


def solve():

    def hanoi(n, one, two, three):
        nonlocal result
        nonlocal visited

        if n == 0:
            return

        hanoi(n - 1, one, three, two)
        result += 1
        visited.append((one, three))
        hanoi(n - 1, two, one, three)

    result = 0
    visited = []
    hanoi(n, 1, 2, 3)
    print(result)
    [print(*footprint) for footprint in visited]


solve()
