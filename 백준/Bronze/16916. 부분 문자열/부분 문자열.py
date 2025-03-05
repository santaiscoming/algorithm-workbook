import sys

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T, P = input().rstrip(), input().rstrip()


def solution():
    def kmp():
        lps = [0] * len(P)
        matched = 0
        i = 1

        while i < len(P):
            if P[matched] == P[i]:
                matched += 1
                lps[i] = matched
                i += 1

            else:
                if matched != 0:
                    matched = lps[matched - 1]
                else:
                    i += 1

        t = p = 0
        result = []

        while t < len(T):
            if T[t] == P[p]:
                t += 1
                p += 1

                if p == len(P):
                    result.append(t - p + 1)
                    p = lps[p - 1]
            else:
                if p != 0:
                    p = lps[p - 1]
                else:
                    t += 1

        return result

    print(1) if len(kmp()) >= 1 else print(0)


solution()
