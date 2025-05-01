import sys
import math


# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

arr = [s for s in iter(lambda: input().rstrip(), ".")]


def solution():
    def isBalance(s: str) -> bool:
        brackets = list(filter(lambda x: x in ["[", "]", "(", ")"], list(s)))
        stack = []

        for b in brackets:
            if not stack or b in ["[", "("]:
                stack.append(b)
                continue

            if stack and b in ["]", ")"]:
                if stack[-1] == "[" and b == "]":
                    stack.pop()
                elif stack[-1] == "(" and b == ")":
                    stack.pop()
                else:
                    stack.append(b)

        return True if not stack else False

    for s in arr:
        print("yes") if isBalance(s) else print("no")


solution()
