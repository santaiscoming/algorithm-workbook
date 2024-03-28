import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

N = int(input())
nodes = [input().split() for _ in range(N)]
tree = {}

for node, left, right in nodes:
    tree[node] = (left, right)


def solution2(root):
    pre_order_acc = []
    in_order_record = []
    post_order_record = []

    pre_order("A", pre_order_acc)
    in_order("A", in_order_record)
    post_order("A", post_order_record)

    print("".join(pre_order_acc))
    print("".join(in_order_record))
    print("".join(post_order_record))


def solution(root, tree):
    print(pre_order(root, tree))
    print(in_order(root, tree))
    print(post_order(root, tree))


# 방문 -> 왼 -> 오
def pre_order(node, tree):
    if node == ".":
        return ""

    left, right = tree[node]

    return node + pre_order(left, tree) + pre_order(right, tree)

    # # 트리 방문
    # acc.append(node)

    # left, right = tree[node]
    # pre_order(left, acc)
    # pre_order(right, acc)


# 왼 -> 방문 -> 오
def in_order(node, tree):
    if node == ".":
        return ""

    left, right = tree[node]

    return in_order(left, tree) + node + in_order(right, tree)

    # left, right = tree[node]
    # in_order(left, acc)
    # # 트리 방문
    # acc.append(node)
    # in_order(right, acc)


# 왼 -> 오 -> 방문
def post_order(node, tree):
    if node == ".":
        return ""

    # left, right = tree[node]
    # post_order(left, acc)
    # post_order(right, acc)
    # # 트리 방문
    # acc.append(node)

    left, right = tree[node]

    return post_order(left, tree) + post_order(right, tree) + node


solution("A", tree)
