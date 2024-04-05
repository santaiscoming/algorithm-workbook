import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]


def solution(K):
    count = 0
    ascending_coins = sorted(coins, reverse=True)

    for i in range(N):
        cur_coin = ascending_coins[i]
        # 코인을 돌면서 K를 깍아준다
        # if K가 현재 코인보다 작다면 다음 코인으로 넘어간다
        max_coin_cnt = K // cur_coin
        K -= max_coin_cnt * cur_coin
        count += max_coin_cnt

        if K == 0:
            return count

    return count


result = solution(K)
print(result)
