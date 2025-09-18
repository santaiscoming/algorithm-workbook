import sys

# sys.stdin = open("input.txt", "r")  # ❌
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def solve():
    def mergeSort(arr):
        nonlocal swapCnt

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        leftHalf = mergeSort(arr[:mid])
        rightHalf = mergeSort(arr[mid:])

        newArr = []
        i, j = 0, 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                newArr.append(leftHalf[i])
                i += 1
            else:
                swapCnt += len(leftHalf) - i
                newArr.append(rightHalf[j])
                j += 1

        while i < len(leftHalf):
            newArr.append(leftHalf[i])
            i += 1

        while j < len(rightHalf):
            newArr.append(rightHalf[j])
            j += 1

        return newArr

    swapCnt = 0
    mergeSort(arr)
    print(swapCnt)

    pass


solve()
