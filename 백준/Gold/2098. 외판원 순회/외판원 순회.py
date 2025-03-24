import sys
import math

input = sys.stdin.readline  

n = int(input()) 


def solution():
    def isIn(i, A):
        """도시 i가 집합 A에 포함되어 있는지 확인"""
        return (A & (1 << (i - 2))) != 0  # 비트마스크로 도시 i가 집합 A에 있는지 확인
        # i-2를 사용하는 이유: 도시는 1부터 시작하지만 비트는 0부터 시작하고, 도시 1은 항상 시작점이므로 제외

    def diff(A, j):
        """집합 A에서 도시 j를 제거"""
        return A & ~(1 << (j - 2))  # 비트마스크에서 j에 해당하는 비트를 끄기

    def count(A, n):
        """집합 A에 포함된 도시의 수 계산"""
        count = 0
        for i in range(n - 1):  # n-1개 도시(2번 도시부터 n번 도시까지)
            if A & (1 << i):  # i번째 비트가 켜져 있으면
                count += 1
        return count

    def path(P, start, A):
        """최적 경로 복원"""
        path = [start]  # 시작 도시로 경로 초기화
        current = start  # 현재 도시를 시작 도시로 설정
        while A > 0:  # 모든 도시를 방문할 때까지
            next_city = P[current][A]  # 현재 상태에서 다음에 방문할 도시
            path.append(next_city)  # 경로에 다음 도시 추가
            A = diff(A, next_city)  # 방문한 도시를 집합에서 제거
            current = next_city  # 현재 도시 업데이트
        path.append(start)  # 시작점으로 돌아오기

        return path

    def minimum(W, D, i, A):
        """집합 A의 도시들을 방문한 후 i로 가는 최소 비용과 경로 계산"""
        minValue = math.inf  # 최소값 초기화
        minJ = 1  # 최소값을 주는 도시 초기화
        n = len(W) - 1  # 도시 수 (0번 인덱스는 사용하지 않음)

        for j in range(2, n + 1):  # 2번 도시부터 n번 도시까지
            if isIn(j, A):  # j가 집합 A에 포함된 경우
                m = (
                    W[i][j] + D[j][diff(A, j)]
                )  # i에서 j로 가는 비용 + j에서 A-{j}를 방문하고 시작점으로 돌아가는 비용
                if minValue > m:  # 더 작은 비용을 찾으면
                    minValue = m  # 최소값 갱신
                    minJ = j  # 최소값을 주는 도시 갱신

        return minValue, minJ  # 최소 비용과 해당 도시 반환

    def travel(w):
        n = len(w) - 1  # 도시 수
        size = 2 ** (n - 1)  # 가능한 부분집합 수 (도시 2~n에 대해)

        D = [[0] * size for _ in range(n + 1)]  # 최소 비용 저장 배열
        P = [[0] * size for _ in range(n + 1)]  # 이전 도시 저장 배열

        for i in range(2, n + 1):  # 모든 도시에 대해
            D[i][0] = w[i][1]  # 도시 i에서 시작 도시(1)로 직접 돌아가는 비용

        # 방문할 도시 수에 따라 DP 테이블 채우기
        for k in range(1, n - 1):  # 방문할 도시 수 (1개부터 n-2개까지)
            for A in range(1, size):  # 모든 부분집합에 대해
                if count(A, n) == k:  # 크기가 k인 부분집합만 처리
                    for i in range(2, n + 1):  # 모든 도시에 대해
                        if not isIn(
                            i, A
                        ):  # i가 A에 없는 경우만 처리 (i에서 A를 방문하고 1로 돌아감)
                            D[i][A], P[i][A] = minimum(
                                w, D, i, A
                            )  # 최소 비용과 다음 도시 계산

        # 주석 처리된 코드는 다른 접근 방식으로 보이며 현재 사용되지 않음

        A = size - 1  # 모든 도시를 포함하는 집합
        D[1][A], P[1][A] = minimum(
            w, D, 1, A
        )  # 시작 도시에서 모든 도시를 방문하는 최소 비용

        return D, P  # 계산된 DP 테이블 반환

    w = [[0] * (n + 1) for _ in range(n + 1)]  # 비용 행렬 초기화

    # 도시 간 비용 입력 받기
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            w[i][j] = (
                row[j - 1] if row[j - 1] > 0 else math.inf
            )  # 경로가 없는 경우(0) 무한대로 설정

    D, P = travel(w)  # 최소 비용 및 경로 계산

    A_final = 2 ** (n - 1) - 1  # 모든 도시를 포함하는 집합
    min_cost = D[1][A_final]  # 시작 도시에서 모든 도시를 방문하고 돌아오는 최소 비용

    print(min_cost)  # 결과 출력


solution()  # 함수 실행
