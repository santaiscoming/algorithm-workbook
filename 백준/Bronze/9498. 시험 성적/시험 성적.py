import sys

sys.setrecursionlimit(10**8)
# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

exam_score = int(input())

grade_dict = {10: "A", 9: "A", 8: "B", 7: "C", 6: "D"}


print(grade_dict.get(exam_score // 10, "F"))
