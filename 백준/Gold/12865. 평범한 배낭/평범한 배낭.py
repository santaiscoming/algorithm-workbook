import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline
# N : 물품개수, K : 무게
N, K = map(int, input().split())
# (W, V) : 무게, 가치
items = [list(map(int, input().split())) for _ in range(N)]


def solution(items):
    table = [[0] * (K + 1) for _ in range(N + 1)]

    for y in range(1, N + 1):
        cur_w, cur_v = items[y - 1]

        for bag_w in range(K + 1):
            prev_item_table_acc = table[y - 1][bag_w]

            if bag_w >= cur_w:
                max_cur_item_val = table[y - 1][bag_w - cur_w] + cur_v
                table[y][bag_w] = max(max_cur_item_val, prev_item_table_acc)
            else:
                table[y][bag_w] = prev_item_table_acc

    print(table[-1][-1])


solution(items)
