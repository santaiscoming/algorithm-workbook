import sys

# sys.setrecursionlimit(10**8)
input = sys.stdin.readline
#sys.stdin = open("./input.txt", "r")  # 제거


# A, B = map(int, input().split(" "))
A, B = [int(i) for i in input().split(" ")]


print(A + B)
print(A - B)
print(A * B)
print(int(A / B))
print(A % B)
