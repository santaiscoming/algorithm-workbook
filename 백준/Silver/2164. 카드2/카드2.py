import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
cards = [i + 1 for i in range(N)]


def solution(N, cards):
    idx = 0

    while True:

        if idx % 2 == 0:
            idx += 1
            if idx == len(cards):
                print(cards[idx - 1])
                return
        else:
            cards.append(cards[idx])
            idx += 1


solution(N, cards)
