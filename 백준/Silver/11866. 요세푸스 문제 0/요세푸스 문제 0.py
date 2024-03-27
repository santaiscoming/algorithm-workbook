import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, K = [int(num) for num in input().split(" ")]


class Queue:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.que = [None] * capacity

    def enque(self, value):
        self.que[self.rear] = value
        self.rear += 1
        self.count += 1

        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        result = self.que[self.front]
        self.front += 1
        self.count -= 1

        if self.front == self.capacity:
            self.front = 0

        return result

    def is_full(self):
        return self.capacity >= self.count

    def is_empty(self):
        return


def solution(N, K):
    result = []
    queue = Queue(N)

    for i in range(1, N + 1):
        queue.enque(i)

    while queue.count:
        for _ in range(K - 1):
            val = queue.deque()
            queue.enque(val)

        pick_person = queue.deque()
        result.append(pick_person)

    return result


result = "<" + ", ".join(list(map(str, solution(N, K)))) + ">"

print(result)
