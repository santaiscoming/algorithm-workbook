import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())


def solution():
    def get분해합(num):
        return sum([int(n) for n in str(num)], num)

    try:
        print(min(i for i in range(n) if get분해합(i) == n))
    except:
        print(0)


solution()
