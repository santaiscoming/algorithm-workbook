import sys

# sys.stdin = open("./input.txt", "r")
sys.setrecursionlimit(10**6)

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


N = int(input())
# vertexes = [list(map(int, vertex.split())) for vertex in readlines(N - 1)]
vertexes = [list(map(int, input().split())) for _ in range(N - 1)]


def solution(N, vertexes):
    visited = {i: False for i in range(1, N + 1)}
    graph = {i: [] for i in range(1, N + 1)}
    result = {i: 0 for i in range(1, N + 1)}

    for vertex in vertexes:
        a, b = vertex
        graph[a].append(b)
        graph[b].append(a)

    def dfs(graph, start, visited, result):
        visited[start] = True

        for vertex in graph[start]:
            if not visited[vertex]:
                result[vertex] = start
                dfs(graph, vertex, visited, result)

    dfs(graph, 1, visited, result)

    return result


[print(result) for result in solution(N, vertexes).values() if result != 0]
