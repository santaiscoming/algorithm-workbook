import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline


N = int(input())
time_line = [list(map(int, input().split())) for _ in range(N)]


def solution(N, time_line):
    # 끝나는 시간으로 정렬한다
    # 현재 끝난시간을 저장한다
    # 끝난시간이 업데이트 될떄마다 cnt += 1
    cnt = 0
    cur_time = 0

    end_sorted_time_line = sorted(time_line, key=lambda x: (x[1], x[0]))
    last_meeting_start, last_meeting_end = end_sorted_time_line[-1]

    # while last_meeting_start >= cur_time:
    #     start_idx = 0
    #     for i in range(start_idx, N):
    #         print(start_idx)
    #         start, end = end_sorted_time_line[i]
    #         if cur_time <= start:
    #             start_idx = i + 1
    #             cur_time = end
    #             cnt += 1
    #             break

    # print(cnt)

    for start, end in end_sorted_time_line:
        if start < cur_time:
            continue

        cnt += 1
        cur_time = end

    print(cnt)


solution(N, time_line)
