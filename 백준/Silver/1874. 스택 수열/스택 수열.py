import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]


def solution2():
    stack = []
    result = []
    num = 1

    for target in arr:
        while num <= target:
            result.append("+")
            stack.append(num)
            num += 1

        if stack[-1] == target:
            stack.pop()
            result.append("-")
        else:
            print("NO")
            return

    print("\n".join(result))


solution2()


def solution():
    result = []
    stack = []
    pl = 0

    for i in range(1, n + 1):
        stack.append(i)
        result.append("+")

        curr = arr[pl]
        if stack[-1] >= curr:
            while stack and stack[-1] >= curr:
                result.append("-")
                v = stack.pop()
                pl += 1
                if pl > len(arr) - 1:
                    break
                curr = arr[pl]

    while stack and pl < n:
        curr = arr[pl]
        v = stack.pop()
        pl += 1
        if v == curr:
            result.append("-")
        else:
            print("NO")
            return

    [print(v) for v in result]


# solution()
