import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
tops = [int(top) for top in input().split(' ')]

def solution(tops, N):
    stack = []
    result = [0] * N

    for curr_top_idx in range(N):
        while stack:
            if tops[stack[-1]] < tops[curr_top_idx]:
                stack.pop()
            else:
                break

        if stack:
            result[curr_top_idx] = stack[-1] + 1
        stack.append(curr_top_idx)

    return result

def solution2(tops, N):
    stack = []
    result = [0] * N

    for i in range(N):
        while stack and tops[stack[-1]] < tops[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] + 1
        stack.append(i)

    return result

result = solution(tops, N)

print(' '.join(map(str,result)))

