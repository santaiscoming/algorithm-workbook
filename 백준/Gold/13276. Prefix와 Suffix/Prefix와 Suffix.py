import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

s = input().rstrip()
a = input().rstrip()
b = input().rstrip()


def solution():
    def createLps(pat: str) -> list[int]:
        """
        pat[0..m-1] 에 대해 LPS(Longest Prefix-Suffix) 배열을 만든다.
        lps[i] = pat[0..i]의 접두사 == 접미사 최대 길이.
        시간 : O(m)
        """
        m = len(pat)
        lps = [0] * m
        j = 0  # 현재 일치한 접두사 길이
        for i in range(1, m):
            while j and pat[i] != pat[j]:
                j = lps[j - 1]  # 접두사 길이를 줄여 가며 rollback
            if pat[i] == pat[j]:
                j += 1
                lps[i] = j
        return lps

    def kmpSearch(text: str, pat: str) -> list[int]:
        """
        텍스트에서 패턴이 등장하는 모든 시작 위치를 반환한다.
        시간 : O(n + m)
        """
        if not pat:
            return list(range(len(text) + 1))  # 빈 패턴 처리

        lps = createLps(pat)
        n, m = len(text), len(pat)
        res = []
        j = 0  # 패턴 인덱스

        for i in range(n):  # 텍스트 인덱스
            while j and text[i] != pat[j]:
                j = lps[j - 1]  # 실패 → 패턴 점프
            if text[i] == pat[j]:
                j += 1
                if j == m:  # 패턴 끝까지 매칭
                    res.append(i - m + 1)  # 발견 위치 저장
                    j = lps[j - 1]  # 다음 매칭 탐색 준비
        return res

    kmp1, kmp2 = kmpSearch(s, a), kmpSearch(s, b)
    resultSet = set()

    for y in kmp1:  # A 패턴이 발견된 위치
        for x in kmp2:  # B 패턴이 발견된 위치
            length = x + len(b) - y
            if length < len(a) or length < len(b):
                continue

            resultSet.add(s[y : x + len(b)])

    print(len(resultSet))


solution()
