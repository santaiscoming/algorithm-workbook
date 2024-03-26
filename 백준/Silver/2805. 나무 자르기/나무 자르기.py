import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N, M = [int(i) for i in input().split()]
trees = [int(tree) for tree in input().split()]

# 절단기 최대 높이는 max(trees)

def get_cutting_tree_height(arr, count):
    result = 0
    
    for tree_height in arr:
      if(tree_height < count):
        continue
      result += tree_height - count

    return result



def solution(trees, M):
    left = 1
    right = max(trees)
    result = 0

    while left <= right:
        center = (left + right) // 2
        cutting_tree_height = get_cutting_tree_height(trees, center)

        if cutting_tree_height >= M:
            result = center
            left = center + 1
        else:
            right = center - 1

    return result

print(solution(trees, M))