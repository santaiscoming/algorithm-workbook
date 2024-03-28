import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())

result = 0


def solution(N, firstNum):
    global result

    result += 1
    copy = str(firstNum)

    if int(copy) <= 10:
        copy = "0" + str(copy)

    new_num = int(str(firstNum)[-1] + str(sum([int(char) for char in copy]) % 10))

    if new_num == N:
        return
    else:
        solution(N, new_num)


solution(N, N)
print(result)
