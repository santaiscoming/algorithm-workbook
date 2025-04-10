import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]


def solution():
    houses.sort()
    result = 0

    # left: 공유기 사이의 최소 거리
    # right: 공유기 사이의 최대 거리
    # mid: 최적의 결정값
    left = 1
    right = houses[-1] - houses[0]

    while left <= right:
        mid = (left + right) // 2

        last_router_position = houses[0]
        installed_count = 1

        for i in range(1, n):
            current_house_position = houses[i]
            distance = current_house_position - last_router_position

            if distance >= mid:
                installed_count += 1
                last_router_position = current_house_position

        if installed_count >= c:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    print(result)


solution()
