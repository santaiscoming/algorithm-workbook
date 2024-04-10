import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline


N = int(input())
time_line = [list(map(int, input().split())) for _ in range(N)]


def solution(N, time_line):
    cnt = 0
    cur_time = 0

    # 끝나는 시간(x[1]) 기준으로 정렬하고 만약 같다면 x[0]으로 정렬한다.
    end_sorted_time_line = sorted(time_line, key=lambda x: (x[1], x[0]))

    for start, end in end_sorted_time_line:
        if start < cur_time:
            continue

        cnt += 1
        cur_time = end

    print(cnt)


solution(N, time_line)
