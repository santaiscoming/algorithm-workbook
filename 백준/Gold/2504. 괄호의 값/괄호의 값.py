import sys


# sys.stdin = open("./input.txt", "r")  # 제거
input = sys.stdin.readline

string = input().rstrip()


def solution():
    stack = []

    for char in string:
        if char in ["(", "["]:  # open
            stack.append(char)
        else:  # close
            if not stack:
                print(0)
                return

            if char == ")":
                if stack[-1] == "(":  # 바로 괄호쌍이 만들어지는 경우
                    stack.pop()  # '(' 제거
                    stack.append(2)  # 값 2 추가
                else:
                    temp = 0
                    # 닫는 괄호 전까지의 값들을 모두 더함
                    while stack and isinstance(stack[-1], int):
                        temp += stack.pop()

                    # 짝이 맞는지 확인
                    if not stack or stack[-1] != "(":
                        print(0)
                        return

                    stack.pop()  # '(' 제거
                    stack.append(temp * 2)  # 괄호 안의 값 * 2

            elif char == "]":
                if stack[-1] == "[":  # 바로 괄호쌍이 만들어지는 경우
                    stack.pop()  # '[' 제거
                    stack.append(3)  # 값 3 추가
                else:
                    temp = 0
                    # 닫는 괄호 전까지의 값들을 모두 더함
                    while stack and isinstance(stack[-1], int):
                        temp += stack.pop()

                    # 짝이 맞는지 확인
                    if not stack or stack[-1] != "[":
                        print(0)
                        return

                    stack.pop()  # '[' 제거
                    stack.append(temp * 3)  # 괄호 안의 값 * 3

    # 모든 처리 후 스택에는 숫자만 남아있어야 함
    if any([not isinstance(x, int) for x in stack]):
        print(0)
        return

    print(sum(stack))


solution()
