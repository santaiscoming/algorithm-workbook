import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

t = int(input())
arr = [input().strip() for _ in range(t)]


def solution():
    def isValid(str: chr) -> bool:
        stack = []

        for c in str:
            if c == "(":
                stack.append(c)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)

        return True if not stack else False

    for str in arr:
        if isValid(str):
            print("YES")
        else:
            print("NO")


solution()
