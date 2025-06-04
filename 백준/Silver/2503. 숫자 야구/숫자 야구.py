import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
answers = [list(map(int, input().split())) for _ in range(n)]


def solution():
    def create_all_cases(nums, visited):
        if len(nums) == 3:
            return [int("".join(map(str, nums)))]

        result = []
        for i in range(1, 10):
            if not visited[i]:
                visited[i] = True
                result.extend(create_all_cases([*nums, i], visited))
                visited[i] = False

        return result

    def guess(num1, num2):
        num1, num2 = str(num1), str(num2)
        strike, ball = 0, 0

        for i in range(3):
            if num1[i] == num2[i]:
                strike += 1
                continue
            if num1[i] in num2:
                ball += 1

        return strike, ball

    possibleNums = []
    all_cases = set(create_all_cases([], [False] * 10))

    for case in all_cases:
        isPossible = True
        for num, strike, ball in answers:
            g_strike, g_ball = guess(case, num)

            if strike != g_strike or ball != g_ball:
                isPossible = False
                break

        if isPossible:
            possibleNums.append(case)

    print(len(possibleNums))


solution()
