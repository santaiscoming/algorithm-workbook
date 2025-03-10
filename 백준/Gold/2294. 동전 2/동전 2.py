import sys
import math
from collections import deque


# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


def bottomUp():
    memo = [0] + [math.inf] * k

    for i in range(1, k + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], memo[i - coin] + 1)

    print(-1) if memo[k] == math.inf else print(memo[k])

    pass


# bottomUp()


def bfs():
    global coins

    coins = sorted(set(coins))

    visited = [False] * (k + 1)
    queue = deque([(0, 0)])
    visited[0] = True

    while queue:
        current_sum, coin_count = queue.popleft()

        if current_sum == k:
            print(coin_count)
            return

        for coin in coins:
            next_sum = current_sum + coin
            if next_sum <= k and not visited[next_sum]:
                visited[next_sum] = True
                queue.append((next_sum, coin_count + 1))

    print(-1)


bfs()


def topDown():
    memo = {}

    def coin_change(amount):
        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        best = math.inf
        for coin in coins:
            if coin <= amount:
                best = min(best, coin_change(amount - coin) + 1)

        memo[amount] = best
        return best

    ans = coin_change(k)
    if ans == math.inf:
        print(-1)
    else:
        print(ans)


# topDown()
