import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
cookie = [list(input().rstrip()) for _ in range(N)]


def solution(cookie, N):
    head = getHead(cookie)
    heart = (head[0] + 1, head[1])
    leftArm, rightArm = getArms(heart, cookie)
    body = (heart[0] + 1, heart[1])
    body_length, (body_y, body_x) = getBody(body, cookie)
    body_end_axis = (body_y, body_x)
    leftLeg, rightLeg = getLegs(body_end_axis, cookie)

    heart_x, heart_y = heart
    print(heart_x + 1, heart_y + 1)
    print(leftArm, rightArm, body_length, leftLeg, rightLeg)


def getBody(body, cookie):
    y, x = body
    body_length = 0

    for i in range(y, N):
        if cookie[i][x] != "*":
            break

        body_length += 1

    return (body_length, [y + body_length, x])


def getLegs(body, cookie):
    left_y, left_x = (body[0] + 1, body[1] - 1)
    right_y, right_x = (body[0] + 1, body[1] + 1)

    leftLeg = 0
    rightLeg = 0

    for i in range(left_y, N):
        if cookie[i][left_x] != "*":
            break

        leftLeg += 1

    for i in range(right_y, N):
        if cookie[i][right_x] != "*":
            break

        rightLeg += 1

    return (leftLeg + 1, rightLeg + 1)


def getHead(cookie):
    for y in range(len(cookie)):
        for x in range(len(cookie[0])):
            if cookie[y][x] == "*":
                return (y, x)


def getArms(heart, cookie):
    y, x = heart
    leftArm = 0
    rightArm = 0

    for i in range(x - 1, -1, -1):
        if cookie[y][i] == "*":
            leftArm += 1
        else:
            break

    for i in range(x + 1, len(cookie[0])):
        if cookie[y][i] == "*":
            rightArm += 1
        else:
            break

    return (leftArm, rightArm)


solution(cookie, N)
