import sys
import math

# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))


def solution():
    minSum = math.inf
    maxSum = -math.inf

    def calc(op, acc, next):
        match op:
            case 0:  # +
                return acc + next
            case 1:  # -
                return acc - next
            case 2:  # *
                return acc * next
            case 3:  # //

                if acc < 0:
                    return -(abs(acc) // next)

                return acc // next

    def dfs(depth, acc):
        nonlocal minSum
        nonlocal maxSum

        if not any(ops):
            # if depth >= sum(ops):
            minSum = min(minSum, acc)
            maxSum = max(maxSum, acc)
            return

        for i in range(4):
            if ops[i] != 0:
                ops[i] -= 1
                next = nums[depth + 1]
                dfs(depth + 1, calc(i, acc, next))
                ops[i] += 1

    dfs(0, nums[0])

    print(maxSum)
    print(minSum)


solution()
