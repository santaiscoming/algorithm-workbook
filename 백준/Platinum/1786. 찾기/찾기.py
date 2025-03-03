import sys

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T, P = list(input().rstrip()), list(input().rstrip())


def solution():

    result = kmp_match(T, P)
    print(len(result))
    for num in result:
        print(num + 1)


def kmp_match(txt, pattern):
    pt = 1
    pp = 0
    skip = [0] * (len(pattern) + 1)
    result = []

    skip[pt] = 0
    while pt != len(pattern):
        if pattern[pt] == pattern[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = 0
        else:
            pp = skip[pp]

    pt, pp = 0, 0
    while pt != len(txt) and pp != len(pattern):
        if txt[pt] == pattern[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

        if pp == len(pattern):
            result.append(pt - pp)
            pp = skip[pp]

    return result


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
    print(lps)
    positions = []  # 패턴이 일치하는 시작 인덱스를 저장할 리스트
    pt = 0  # text의 인덱스
    pp = 0  # pattern의 인덱스

    while pt < len(text):
        if text[pt] == pattern[pp]:
            pt += 1
            pp += 1

        # 만약 j가 패턴의 끝에 도달하면, 패턴이 발견된 것입니다.
        if pp == len(pattern):
            positions.append(pt - pp)
            # 다음 일치를 위해 j를 lps[j-1]로 이동
            pp = lps[pp - 1]
        elif pt < len(text) and text[pt] != pattern[pp]:
            # 불일치가 발생한 경우
            if pp != 0:
                # 이전에 일치했던 길이를 활용하여 패턴 포인터를 이동
                pp = lps[pp - 1]
            else:
                pt += 1
    return positions


solution()
