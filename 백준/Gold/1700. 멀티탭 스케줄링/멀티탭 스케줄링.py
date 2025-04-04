import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
plugs = list(map(int, input().split()))


def solution():
    multi_tab = [-1] * n
    result = 0

    for i in range(n):
        if not plugs[i] in multi_tab:
            multi_tab[i] = plugs[i]

    def take_victim(search_i):
        victim_idx = 0
        candidate = -1
        checked = []
        for i, inserted_plug in enumerate(multi_tab):
            if inserted_plug == -1:
                return i
            if not inserted_plug in plugs[search_i:]:
                return i

        for j in range(search_i + 1, k):
            for i, inserted_plug in enumerate(multi_tab):
                if (
                    plugs[j] == inserted_plug
                    and j > candidate
                    and not inserted_plug in checked
                ):
                    candidate = j
                    victim_idx = i
                    checked.append(inserted_plug)

        return victim_idx

    for i in range(n, k):
        if plugs[i] in multi_tab:
            continue

        idx = take_victim(i)
        if multi_tab[idx] == -1:
            multi_tab[idx] = plugs[i]
            continue

        multi_tab[idx] = plugs[i]
        result += 1

    print(result)


solution()
