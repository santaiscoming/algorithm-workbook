import sys

# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline


P = int(input())
children = [map(int, input().rstrip().split()) for _ in range(P)]


def solution(children, P):
    result = [0] * (P + 1)

    for child in children:
        case_num, *heights = child

        for idx, heigth in enumerate(heights):
            for idx, heigth in enumerate(heights):
                if idx == 19:
                    break
                if heights[idx] > heights[idx + 1]:
                    heights[idx], heights[idx + 1] = heights[idx + 1], heights[idx]
                    result[case_num] += 1

    for i in range(1, P + 1):
        print(f"{i} {result[i]}")


solution(children, P)
