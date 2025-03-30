import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline
n = int(input())


def solution():
    answer = 0

    for i in range(1, n + 1):
        if i < 100:
            answer += 1
        else:
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
                answer += 1

    print(answer)


solution()
