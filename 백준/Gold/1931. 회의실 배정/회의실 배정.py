import sys

# sys.stdin = open("./input.txt", "r")  
input = sys.stdin.readline


n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]


def solution():
    times.sort(key=lambda x: (x[1], x[0]))
    result = [times[0]]

    for i in range(1, n):
        s, e = times[i]
        ps, pe = result[-1]

        if s >= pe:
            result.append(times[i])

    print(len(result))


solution()
