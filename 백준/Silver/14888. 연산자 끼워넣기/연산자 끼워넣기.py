import sys
import math

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))


def solution():
    min_value = math.inf
    max_value = -math.inf

    def op(op_i, v_1, v_2):
        match op_i:
            case 0:
                return v_1 + v_2
            case 1:
                return v_1 - v_2
            case 2:
                return v_1 * v_2
            case 3:
                if v_1 < 0 and v_2 >= 0:
                    return -(abs(v_1) // v_2)

                return v_1 // v_2

    def dfs(picked, acc):
        nonlocal min_value
        nonlocal max_value

        if picked == n - 1:
            min_value = min(acc, min_value)
            max_value = max(acc, max_value)
            return

        for i in range(4):
            if ops[i] != 0:
                ops[i] -= 1
                dfs(picked + 1, op(i, acc, nums[picked + 1]))
                ops[i] += 1

    dfs(0, nums[0])

    print(max_value)
    print(min_value)


solution()
