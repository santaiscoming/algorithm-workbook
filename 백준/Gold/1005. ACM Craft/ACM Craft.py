import sys
import math
from collections import defaultdict, deque

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

T = int(input())
tc = []
for _ in range(T):
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(k)]
    last = int(input())
    tc.append([n, k, costs, edges, last])


def solve():
    for case in tc:
        n, k, costs, edges, target = case
        indegs = {i + 1: 0 for i in range(n)}
        graph = defaultdict(list)
        for v, u in edges:
            indegs[u] += 1
            graph[v].append(u)

        costs = [0] + costs
        dp = [-math.inf] * (n + 1)
        q = deque()
        for i in range(1, n + 1):
            if indegs[i] == 0:
                q.append(i)
                dp[i] = costs[i]

        while q:
            now = q.popleft()

            for i in graph[now]:
                indegs[i] -= 1
                dp[i] = max(dp[i], dp[now] + costs[i])

                if indegs[i] == 0:
                    q.append(i)

        print(dp[target])


solve()
