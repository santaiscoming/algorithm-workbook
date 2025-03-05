import sys
from typing import List

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T, P = list(input().rstrip()), list(input().rstrip())


def solution():
    def create_lps(pattern: chr) -> List[int]:
        matched = 0
        lps = [0] * len(pattern)
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[matched]:
                matched += 1
                lps[i] = matched
                i += 1
            else:
                if matched != 0:
                    matched = lps[matched - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def kmp1(txt: chr, pattern: chr) -> List[int]:
        result = []
        lps = create_lps(pattern)
        t = p = 0

        while t < len(txt):
            if txt[t] == pattern[p]:
                t += 1
                p += 1

            if p == len(pattern):
                result.append(t - p + 1)
                p = lps[p - 1]
            elif t < len(txt) and txt[t] != pattern[p]:
                if p != 0:
                    p = lps[p - 1]
                else:
                    t += 1

        return result


    def kmp2(txt: chr, pattern: chr) -> List[int]:
        result = []
        lps = create_lps(pattern)
        t = p = 0

        while t < len(txt):
            if txt[t] == pattern[p]:
                t += 1
                p += 1
                if p == len(pattern):
                    result.append(t - p + 1)
                    p = lps[p - 1]
            else:
                if p != 0:
                    p = lps[p - 1]
                else:
                    t += 1

        return result

    result = kmp2(T, P)
    print(len(result))
    for idx in result:
        print(idx)


solution()
