import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(input().strip())


def solution():
    remove_count = k
    stack = []
    for i, v in enumerate(num):
        v = int(v)

        while stack and v > stack[-1] and remove_count > 0:
            stack.pop()
            remove_count -= 1

        stack.append(v)

    if remove_count > 0:
        print("".join(list(map(str, stack[: n - k]))))
        return

    print("".join(list(map(str, stack))))


solution()


def solution():
    maximum_stack_count = n - k
    stack = []
    for i, v in enumerate(num):
        v = int(v)
        appendable_count = maximum_stack_count - len(stack)
        rest = n - i

        while (
            stack
            and v > stack[-1]
            and maximum_stack_count - len(stack) < rest
            and rest > appendable_count
        ):
            stack.pop()

        if maximum_stack_count - len(stack) > 0:
            stack.append(v)

    print("".join(list(map(str, stack))))


# solution()
