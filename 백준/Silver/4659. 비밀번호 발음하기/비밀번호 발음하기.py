import sys
from functools import reduce

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

lines = [line for line in iter(lambda: input().rstrip(), "end")]


def solution(lines):
    result = [False] * len(lines)

    for idx, line in enumerate(lines):
        possible = True

        possible = containVowel(line)
        if not possible:
            result[idx] = False
            continue

        possible = not isContinuedChar(line)

        if possible:
            result[idx] = True

    for idx, possible in enumerate(result):
        str = lines[idx]

        if possible:
            print(f"<{str}> is acceptable.")
        else:
            print(f"<{str}> is not acceptable.")


def containVowel(str):
    vowel = ["a", "e", "i", "o", "u"]

    return any(char in vowel for char in str)


def isContinuedChar(str):
    wordParts = [0] * (len(str))

    count = 0
    for idx in range(0, len(str) - 1):
        if str[idx] == str[idx + 1]:
            if (str[idx] == "e" and str[idx] == "e") or (
                str[idx] == "o" and str[idx] == "o"
            ):
                continue
            else:
                return True
        else:
            count = 0

    for idx in range(0, len(str)):
        vowel = ["a", "e", "i", "o", "u"]

        if str[idx] in vowel:
            wordParts[idx] = 1

    count = 0
    for idx in range(0, len(wordParts) - 1):
        if count == 2:
            print("cout 3")
            return True

        if wordParts[idx] == wordParts[idx + 1]:
            count += 1
            if count == 2:
                return True
        else:
            count = 0
    return False


solution(lines)
