import sys

# sys.stdin = open("./input.txt", "r")

def readlines(count):
    # return list(map(lambda x: input(), range(count)))
    return [input() for _ in range(count)]

N = int(input())
lines = readlines(N)

numStr = ""
result = []

for line in lines:
    for char in line:
        if char.isdigit():
            numStr += char
            continue;
        if char.isalpha() and numStr != "":
            result.append(int(numStr))
            numStr = ""
    if numStr != "":
        result.append(int(numStr))
        numStr = ""

result.sort()

for numStr in result:
    print(numStr)