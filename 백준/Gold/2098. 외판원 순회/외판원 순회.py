import sys
import math
from typing import List, NewType


# sys.stdin = open("./input.txt", "r")  # ❌
input = sys.stdin.readline

CitySet = NewType("CitySet", int)
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]


def mySolution():
    w = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if mat[i - 1][j - 1] == 0:
                w[i][j] = math.inf
            else:
                w[i][j] = mat[i - 1][j - 1]

    # dp[i][A] = i에서 시작해서 A를 거쳐 v1으로 가는 최소 비용
    # A는 비트마스크로 표현
    size = 2 ** (n - 1)  # 8
    dp = [[0] * size for _ in range(n + 1)]
    for i in range(2, n + 1):
        dp[i][0] = w[i][1]  # dp[i][A] A는 집합개수 즉, 공집합은 0

    def onBitCnt(A: int):
        cnt = 0
        # A는 도시의 부분집합이다. 도시개수가 4개일때 1000 (1번은 제외하므로) 3(n-1)개만 돈다
        for i in range(n - 1):
            if A & (1 << i):
                cnt += 1

        return cnt

    def travel():
        # 순회하고자 하는 점화식
        # dp[i][A] = {2<=j<=n}minimal(w[i][j] + dp[j][A - {Vj}])

        for k in range(
            1, n - 1
        ):  # V1, Vi는 제외, k의 의미 : 부분집합이 k(1,2...)개 일때 공집합인 경우는 이미 처리함
            # k : 1 -> 부분집합이 1개일때
            # K : 2 -> 부분집합이 2개일때
            # 즉, 모든 부분집합 개수에 대해 처리하겠다
            for A in range(1, size):  # range: n = 4 -> citySet 001(1) ~ 111(7)
                # A에 포함되면 방문했다는 얘기..?
                # k:1 -> 걸리는 A: 001, 010, 100
                # k:2 -> 걸리는 A: 011, 101, 110
                if onBitCnt(A) == k:
                    for i in range(2, n + 1):  # 1을 제외한 모든 도시
                        minDist = math.inf
                        # 도시 번호 :  4 3 2
                        # 비트     :  0 0 0
                        # A: 거쳐가는 방문할 도시 so, i에서 시작해 A를 거쳐가므로 A에는 i가 포함되지 않을때만 방문
                        if A & (1 << (i - 2)) == 0:
                            minValue = math.inf

                            for j in range(2, n + 1):
                                if A & (1 << (j - 2)):
                                    m = w[i][j] + dp[j][A & ~(1 << (j - 2))]
                                    if minValue > m:
                                        minValue = m

                            dp[i][A] = minValue
        A = size - 1
        minValue = math.inf

        for j in range(2, n + 1):
            if A & (1 << (j - 2)):
                m = w[1][j] + dp[j][A & ~(1 << (j - 2))]
                if minValue > m:
                    minValue = m

        dp[1][A] = minValue
        print(dp[1][A])

    travel()


mySolution()