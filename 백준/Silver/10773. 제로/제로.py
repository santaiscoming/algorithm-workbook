import sys

 #sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

k = int(input())
arr = [int(input()) for _ in range(k)]


def solution():
    result = [] 

    for op in arr:
        if op == 0:
            result.pop()
        else:
            result.append(op)

    print(sum(result))


solution()
