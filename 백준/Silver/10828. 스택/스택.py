import sys


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
operations = [input().rstrip().split() for _ in range(N)]


def isPush(operations):
    return len(operations) == 2


def solution(operations, N):
    # push : 스택에 넣기
    # pop : 가장 위에 정수 뺴고 출력 (if 있으면 val 없으면 -1)
    # size : len(stack) 출력
    # empty : if  empty 1 else 0 출력
    # top : 가장 위에 있는 정수 출력
    result = []

    for i in range(N):

        if isPush(operations[i]):
            _, val = operations[i]
            result.append(val)

        else:
            operation = operations[i][0]
            resultLength = len(result)

            if operation == "top":
                if resultLength == 0:
                    print(-1)
                else:
                    print(result[resultLength - 1])
                continue
            if operation == "size":
                print(resultLength)
                continue

            if operation == "empty":
                if resultLength != 0:
                    print(0)
                else:
                    print(1)
                continue

            if operation == "pop":
                if resultLength == 0:
                    print(-1)
                else:
                    print(result.pop())
                continue


solution(operations, N)
