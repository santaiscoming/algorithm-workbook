import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

doc, word = input().rstrip(), input().rstrip()


def solution():
    result = 0
    i = 0

    while i <= len(doc) - len(word):
        if doc[i:].startswith(word):
            result += 1
            i += len(word)
        else:
            i += 1

    print(result)


solution()
