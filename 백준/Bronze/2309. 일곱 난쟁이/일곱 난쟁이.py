import sys
from functools import reduce


sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

hobits = [int(input()) for _ in range(9)]
visited = [False] * 9
results = []


def dfs(hobits, result):
    global results

    # result가 100 and len(result) == 7 => return
    if len(result) == 7 and reduce(lambda prev, curr: prev + curr, result) == 100:
        results = result[:]
        return

    for idx, hobit in enumerate(hobits):
        if visited[idx]:
            continue

        visited[idx] = True
        result.append(hobit)
        dfs(hobits, result)
        visited[idx] = False
        result.pop()

        if results:
            return


def solution(hobits):
    result = []

    dfs(hobits, result)
    results.sort()

    for hobit in results:
        print(hobit)


solution(hobits)
