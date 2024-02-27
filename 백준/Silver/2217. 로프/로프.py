import sys
input = sys.stdin.readline

# sys.stdin = open("./input.txt", "r")


def readlines(count):
    # return list(map(lambda x: input(), range(count)))
    return [input() for _ in range(count)]


N = int(input())
ropes = list(map(int, readlines(N)))


def solution(N, ropes):
    result = []
    ascendingRopes = sorted(ropes, reverse=True)

    for i in range(N):
        ropeCount = i + 1
        weight = ascendingRopes[i] * ropeCount
        result.append(weight)

    return max(result)


print(solution(N, ropes))