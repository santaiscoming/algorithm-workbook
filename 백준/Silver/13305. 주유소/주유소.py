import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))


def solution(N, roads, price):
    spend_money = 0
    min_price = price[0]

    for idx in range(len(roads)):
        if price[idx] < min_price:
            min_price = price[idx]
        spend_money += min_price * roads[idx]

    print(spend_money)


solution(N, roads, price)
