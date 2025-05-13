import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

a, b = input().rstrip(), input().rstrip()


def solution():
    memo = []
    for i in range(len(a)):
        flag = False
        for j in range(len(b)):
            ai = i + j
            if ai >= len(a):
                print(len(memo))
                return

            if a[ai] != b[j]:
                flag = True
                break
        if not flag:
            if memo and memo[-1] >= i:
                continue
            memo.append(i + len(b) - 1)

    print(len(memo))


solution()
