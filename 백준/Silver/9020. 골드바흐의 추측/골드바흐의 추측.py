import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for i in range(T)]


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def goldbach_partition(num):
    # 두수의 가장 작은 차이 :
    # 중앙값에서 시작해 벌어지다가 가장 먼저 만나는 값이 차이가 제일 적다
    a, b = num // 2, num // 2

    while a > 1:
        if is_prime(a) and is_prime(b):
            return [a, b]
        a -= 1
        b += 1


for num in nums:
    a, b = goldbach_partition(num)
    print(a, b)
