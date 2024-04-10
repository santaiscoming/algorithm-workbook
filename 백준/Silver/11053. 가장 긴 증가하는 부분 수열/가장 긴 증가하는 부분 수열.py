import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


def solution(N, nums):
    # 아무것도 사용하지 않는경우를 계산하고 nums의 시작숫자와 index를 맞춰주기위해
    nums = [0] + nums
    dp = [0] * (N + 1)

    # now : 현재 선택할 숫자의 idx
    # dp[now] : 현재 선택된 숫자(nums[now])의 증가하는 수열 개수

    # prev : 현재 선택된 index now 이전까지 비교할 숫자의 idx
    # ex)
    # 현재 선택된 숫자 : 30
    # 돌아야할 숫자 : 10[0] 20[1] 10[2] -> [] : idx
    for now in range(1, N + 1):
        cur_num = nums[now]
        for prev in range(0, now):
            prev_num = nums[prev]

            # 현재 선택된 숫자 30 보다 크다면 셀 필요가 없다
            # -> 30이전에 40이 있다면 30보다 큰 수가 앞에 있으니 건너뛴다
            if prev_num >= cur_num:
                continue
            # 자신의 증가하는 수열 개수는 0으로 초기화 되어 있기에
            # prev 즉, (0, 1, ... now-1) 까지 돌면서 10에서 1, 20에서 2, 자신에서 dp[20이라는 숫자의 idx]+ 1 로 업데이트가 된다
            dp[now] = max(
                dp[now], dp[prev] + 1
            )  # +1이라는것은  nums[i] 본인을 사용한것

    print(max(dp))


solution(N, nums)
