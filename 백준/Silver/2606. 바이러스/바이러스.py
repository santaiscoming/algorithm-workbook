import sys

# sys.stdin = open("./input.txt", "r")


def readlines(count=1):
    # result = []

    # while True:
    #     try:
    #         response = input()
    #         print(response)
    #         result.append(response)
    #     except EOFError:
    #         break

    # return result
    return [input() for _ in range(count)]


computer_count = int(input())
network_count = int(input())
networks = [list(map(int, input().split())) for _ in range(network_count)]


def solution(computer_count, network_count, networks):
    visited = {i: False for i in range(computer_count + 1)}
    graph = {i: [] for i in range(computer_count + 1)}
    result = 0

    for network in networks:
        a, b = network
        graph[a].append(b)
        graph[b].append(a)

    def dfs(graph, start, visited):
        visited[start] = True

        for computer_id in graph[start]:
            if not visited[computer_id]:
                dfs(graph, computer_id, visited)

    dfs(graph, 1, visited)

    for computer_id in range(2, computer_count + 1):
        if visited[computer_id]:
            result += 1

    return result


print(solution(computer_count, network_count, networks))
