import sys
from functools import reduce


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]


def my_sort(word):
    return len(word), word


def solution(words, N):
    not_duplicated_list = list(set(words))
    not_duplicated_list.sort(key=my_sort)
    return not_duplicated_list


sorted_list = solution(words, N)

for word in sorted_list:
    print(word)
