import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# N : rank에 있는 점수 개수
# taesu : 태수 점수
# P : rank에 올라갈 수 있는 점수 개수
N, taesu, P = map(int, input().split())
scores = list(map(int, input().split()))


def solution(N, taesu, P, scores: list):
    if N == 0:
        print(1)
        return

    # rank에 점수가 꽉차있고 꼴등보다 태수 점수가 낮을때
    if N == P and scores[-1] >= taesu:
        print(-1)
        return

    for i in range(N):
        cur_score = scores[i]

        if taesu >= cur_score:
            print(i + 1)
            return

        if i == N - 1:
            print(i + 2)
            return


solution(N, taesu, P, scores)
