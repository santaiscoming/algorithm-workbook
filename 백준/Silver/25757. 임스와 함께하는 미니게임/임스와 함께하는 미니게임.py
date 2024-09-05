import sys
import math

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, game_mode = input().split()

people = [input().rstrip() for _ in range(int(N))]


def solution(people, game_mode):
    not_duplicated_people = set(people)
    cnt = convertToPeopleCount(game_mode)

    print(((len(not_duplicated_people)) // cnt))


def convertToPeopleCount(game_mode):
    match game_mode:
        case "Y":
            return 1
        case "F":
            return 2
        case "O":
            return 3


solution(people, game_mode)
