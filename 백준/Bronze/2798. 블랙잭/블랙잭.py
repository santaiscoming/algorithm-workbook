import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))


def solution():
    result = 0
    
    card_dict = {}
    for i, card in enumerate(cards):
        card_dict[card] = i
    
    for i in range(n):
        for j in range(i+1, n):
            two_sum = cards[i] + cards[j]
            remaining = m - two_sum
            
            if remaining > 0 and remaining in card_dict:
                k = card_dict[remaining]
                if k != i and k != j:  # 중복 선택 방지
                    result = max(result, two_sum + remaining)
    
    if result == 0:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    card_sum = cards[i] + cards[j] + cards[k]
                    if card_sum <= m and card_sum > result:
                        result = card_sum
    
    print(result)

solution()
