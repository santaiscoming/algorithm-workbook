import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

X = input().rstrip()
Y = input().rstrip()


def lcs(X_word, Y_word):
    X_len = len(X_word) + 1
    Y_len = len(Y_word) + 1

    table = [[0] * (X_len) for _ in range(Y_len)]

    for y in range(1, Y_len):
        for x in range(1, X_len):
            x_char = X_word[x - 1]
            y_char = Y_word[y - 1]

            if x_char == y_char:
                prev_match = table[y - 1][x - 1]
                table[y][x] = prev_match + 1

            # 문자가 다른경우
            else:
                top = table[y - 1][x]
                left = table[y][x - 1]

                table[y][x] = max(left, top)

    return table[Y_len - 1][X_len - 1]


def solution(X_word, Y_word):
    result = lcs(X_word, Y_word)

    print(result)


solution(X, Y)
