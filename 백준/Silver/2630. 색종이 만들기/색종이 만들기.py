import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(N)]
white = 0
blue = 0


def solution(paper, x, y, N):
    global white
    global blue

    color = int(paper[x][y])
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                solution(paper, x, y, N // 2)  # 1사분면
                solution(paper, x, y + N // 2, N // 2)  # 2사분면
                solution(paper, x + N // 2, y, N // 2)  # 3사분면
                solution(paper, x + N // 2, y + N // 2, N // 2)  # 4사분면
                return
    if color == 1:
        blue += 1
    elif color == 0:
        white += 1


solution(matrix, 0, 0, N)

print(white)
print(blue)
