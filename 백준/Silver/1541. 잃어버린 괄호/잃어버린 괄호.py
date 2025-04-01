import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

s = input()


def solution():
    char = ""
    stack = []
    for i, c in enumerate(s):
        if c == "-" or c == "+":
            if len(char) > 0:
                stack.append(int(char))
                char = ""
            stack.append(c)
        else:
            char += c
            if i == len(s) - 1:
                stack.append(int(char))

    result = stack[0]
    minus_mode = False

    for i in range(1, len(stack), 2):
        if i + 1 < len(stack):
            op = stack[i]
            num = stack[i + 1]

            if op == "-" or minus_mode:
                minus_mode = True
                result -= num
            else:
                result += num

    print(result)


solution()
