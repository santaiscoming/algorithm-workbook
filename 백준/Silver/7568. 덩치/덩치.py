import sys

# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

N = int(input())
people = [[int(num) for num in input().split()] for _ in range(N)]


def solution(N, people):
    result = [1] * len(people)

    for currIdx, currPerson in enumerate(people):
        currW, currH = currPerson
        biggerThan = 0

        for compIdx, compPerson in enumerate(people):
            if currIdx == compIdx:
                continue

            compW, compH = compPerson

            if compW > currW and compH > currH:
                result[currIdx] += 1

    for rank in result:
        print(rank)


solution(N, people)
