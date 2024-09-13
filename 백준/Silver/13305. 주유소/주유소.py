import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))


def solution(N, roads, price):
    skip_idx = None
    spend_money = 0
    min_price = min(price)

    for idx, cur_road in enumerate(roads):
        if skip_idx == idx and skip_idx is not None:
            continue

        curr_price = price[idx]

        if price[idx] == min_price:
            rest_distance = sum(roads[idx:])
            spend_money += min_price * rest_distance
            break

        if idx != len(roads) - 1:
            next_price = price[idx + 1]

            if next_price > curr_price:
                next_road = roads[idx + 1]
                spend_money += (curr_price * next_road) + (cur_road * curr_price)
                skip_idx = idx + 1
            else:
                spend_money += cur_road * curr_price

    print(spend_money)


solution(N, roads, price)
