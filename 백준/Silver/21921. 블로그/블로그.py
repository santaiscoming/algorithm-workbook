import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(map(int, input().split()))


def solution(N, X, visit):
    curr_sum = sum(visit[:X])
    max_sum = curr_sum
    max_count = 1

    for i in range(X, N):
        prev = visit[i - X]
        next = visit[i]
        curr_sum = curr_sum - prev + next

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_count = 1
        elif curr_sum == max_sum:
            max_count += 1

    if max_sum == 0:
        print("SAD")
    else:
        print(max_sum)
        print(max_count)


solution(N, X, visit)
