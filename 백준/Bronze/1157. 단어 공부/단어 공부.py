import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

word = input().rstrip()


def solution(word: str):
    char_obj = {}
    word = word.lower()

    for char in word:
        if not (char in char_obj):
            char_obj[char] = 1
        else:
            char_obj[char] += 1

    max_char_cnt = max(char_obj.values())

    if len(list(filter(lambda num: num == max_char_cnt, char_obj.values()))) > 1:
        print("?")
        return

    for key, val in char_obj.items():
        if val == max_char_cnt:
            print(key.upper())
            return


solution(word)
