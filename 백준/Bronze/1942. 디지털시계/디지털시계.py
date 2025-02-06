import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

global times
times = [input().rstrip().split(" ") for _ in range(3)]


def convert_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))

    return h * 3600 + m * 60 + s


def convert_to_clock_time(seconds):
    seconds = seconds % (24 * 3600)

    h = 0
    while seconds >= 3600:
        h += 1
        seconds -= 3600

    m = 0
    while seconds >= 60:
        m += 1
        seconds -= 60

    s = seconds

    return h * 10000 + m * 100 + s


def solution():
    for start_time, end_time in times:
        start_sec = convert_to_seconds(start_time)
        end_sec = convert_to_seconds(end_time)

        if end_sec < start_sec:
            end_sec += 24 * 3600

        count = 0
        curr = start_sec

        while curr <= end_sec:
            clock_num = convert_to_clock_time(curr % (24 * 3600))

            if clock_num % 3 == 0:
                count += 1

            curr += 1

        print(count)


solution()
