import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

swich_cnt = int(input())
switches = list(map(int, input().split()))
people_cnt = int(input())
people = [list(map(int, input().split())) for _ in range(people_cnt)]


def solution(switches, people):

    for sex, num in people:
        if sex == 1:
            switches = male_toggle(num, switches)
        else:
            switches = female_toggle(num, switches)

    for i in range((swich_cnt // 21) + 1):
        print(" ".join(map(str, map(int, switches[((i) * 20) : ((i + 1) * 20)]))))


def male_toggle(num, switches):
    if num == 1:
        for i in range(len(switches)):
            switches[i] = not switches[i]
    else:
        for i in range(0, len(switches)):
            if (i + 1) % (num) == 0:
                switches[i] = not switches[i]

    return switches


def female_toggle(num, switches):
    start_num = num - 1
    result = None

    for i in range(1, len(switches)):
        _from = start_num - i
        to = start_num + i

        if to > (len(switches) - 1) or _from < 0 or (switches[_from] != switches[to]):
            break

        if switches[_from] == switches[to]:
            result = (_from, to)

    if result is None:
        switches[start_num] = not switches[start_num]
        return switches

    _from, to = result
    for i in range(_from, to + 1):
        switches[i] = not switches[i]

    return switches


solution(switches, people)
