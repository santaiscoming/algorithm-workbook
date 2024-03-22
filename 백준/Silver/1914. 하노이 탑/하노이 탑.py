import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())


# - 원판개수
# - 시작 기둥
# - 옮길 기둥
def hanoi_for_study(N, start_col, end_col, helper_col):
    # 종료조건
    if N == 1:
        print(f"크기{N} disk MOVE ! {start_col} -> {end_col} ")
    else:
        # 문제 정의
        # 1. N개를 옮기기 위해서는 (N-1개)탑을 **이웃**한 기둥으로 옮겨야 한다
        # 1-1. N-1개는 위의 두개인 탑
        # 2. 가장 큰 원반이 최종 기둥으로 간다
        # 3. **이웃**한 원반에서 (N-1개)탑을 목적 기둥으로 간다.
        # 3-1. 이웃한 기둥 : 1에서 옮긴 원반
        # 3-2. N-1개는 이웃기둥으로 옮긴 탑

        hanoi_for_study(N - 1, start_col, helper_col, end_col)  # 1
        print(f"크기{N} disk MOVE ! {start_col} -> {end_col} ")  # 2
        hanoi_for_study(N - 1, helper_col, end_col, start_col)  # 3


def hanoi(disk_count, start_col, end_col, helper_col):
    # 종료조건
    # 마지막(1)디스크가 3번 디스크로 간다 (1번에서)
    if disk_count == 1:
        print(start_col, end_col)
    else:
        # 문제정의
        # 1. N-1개의 덩어리를 시작에서 헬퍼로 옮긴다.
        # 2. N-1개의 덩어리를 헬퍼에서 시작으로 옮긴다.
        hanoi(disk_count - 1, start_col, helper_col, end_col)
        print(start_col, end_col)
        hanoi(disk_count - 1, helper_col, end_col, start_col)


print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)
