import sys

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

L, T = int(input().rstrip()), input().rstrip()


def solution():
    lps = [0] * len(T)
    max_matched = 0
    matched = 0
    i = 1

    while i < len(T):
        if T[i] == T[matched]:
            matched += 1
            max_matched = max(max_matched, matched)
            lps[i] = matched
            i += 1
        else:
            if matched != 0:
                matched = lps[matched - 1]
            else:
                lps[i] = 0
                i += 1

    print(L - lps[-1])


solution()
