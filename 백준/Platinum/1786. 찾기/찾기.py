import sys

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T, P = list(input().rstrip()), list(input().rstrip())


def solution():

    result = kmp_search(T, P)
    print(len(result))
    for num in result:
        print(num + 1)


def compute_lps(pattern):
    """
    패턴에 대한 LPS (Longest Prefix Suffix) 배열을 생성합니다.
    LPS[i]는 pattern[0:i+1] 내에서 proper prefix(전체가 아닌 접두사) 중에서
    suffix(접미사)와 일치하는 최대 길이를 나타냅니다.
    """
    lps = [0] * len(pattern)
    length = 0  # 이전에 일치한 접두사의 길이
    i = 1  # lps[0]은 항상 0이므로 i는 1부터 시작

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # 이전에 일치한 길이를 활용해 fallback 합니다.
                length = lps[length - 1]
                # i는 증가시키지 않고 같은 i에서 다시 비교합니다.
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    텍스트에서 패턴을 KMP 방식으로 검색하여, 패턴이 시작되는 모든 인덱스를 리스트로 반환합니다.
    """
    lps = compute_lps(pattern)
    positions = []  # 패턴이 일치하는 시작 인덱스를 저장할 리스트
    i = 0  # text의 인덱스
    j = 0  # pattern의 인덱스

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        # 만약 j가 패턴의 끝에 도달하면, 패턴이 발견된 것입니다.
        if j == len(pattern):
            positions.append(i - j)
            # 다음 일치를 위해 j를 lps[j-1]로 이동
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            # 불일치가 발생한 경우
            if j != 0:
                # 이전에 일치했던 길이를 활용하여 패턴 포인터를 이동
                j = lps[j - 1]
            else:
                i += 1
    return positions


solution()
