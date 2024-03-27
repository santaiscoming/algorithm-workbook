import sys
from collections import deque

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline


# class Queue:

#     class Empty(Exception):
#         pass

#     class Full(Exception):
#         pass

#     def __init__(self, capacity):
#         self.count = 0
#         self.capacity = capacity
#         self.front = 0
#         self.rear = 0
#         self.que = [None] * capacity

#     def enque(self, value):
#         if self.is_full():
#             raise "꽉 찼습니다 !"

#         self.que[self.rear] = value
#         self.rear += 1
#         self.count += 1

#         if self.rear == self.capacity:
#             self.rear = 0

#     def deque(self):
#         if self.is_empty():
#             return -1

#         result = self.que[self.front]
#         self.front += 1
#         self.count -= 1

#         if self.front == self.capacity:
#             self.front = 0

#         return result

#     def is_full(self):
#         return self.capacity <= self.count

#     def is_empty(self):
#         return 1 if self.count <= 0 else 0

#     def __len__(self):
#         return self.count

#     def peek(self):
#         if not self.que[self.front]:
#             return -1
#         return self.que[self.front]

#     def peek_last(self):
#         if not self.que[self.rear - 1]:
#             return -1

#         return self.que[self.rear - 1]


# def solution(command):
#     result = []
#     queue = Queue(N)

#     for command in commands:

#         if len(command) == 2:
#             method, val = command
#             queue.enque(val)
#             continue

#         command = command[0]
#         if command == "pop":
#             val = queue.deque()
#             result.append(val)
#             continue

#         if command == "size":
#             result.append(len(queue))
#             continue

#         if command == "empty":
#             result.append(queue.is_empty())
#             continue

#         if command == "front":
#             result.append(queue.peek())
#             continue

#         if operation == "back":
#             result.append(queue.peek_last())
#             continue

#     return result

N = int(input())


def solution(N):
    dq = deque()

    for _ in range(N):
        command = sys.stdin.readline().split()

        if command[0] == "push":
            dq.append(int(command[1]))
        elif command[0] == "pop":
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif command[0] == "size":
            print(len(dq))
        elif command[0] == "empty":
            if dq:
                print(0)
            else:
                print(1)
        elif command[0] == "front":
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif command[0] == "back":
            if dq:
                print(dq[-1])
            else:
                print(-1)
    return


solution(N)
