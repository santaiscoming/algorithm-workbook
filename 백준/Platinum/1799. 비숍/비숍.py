import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]


def solution3():
    # 대각선 사용 여부 체크 (우상향 대각선)
    diag_used = [False] * (2 * n)

    def backtrack_diagonal(diagonal_idx):
        if diagonal_idx >= 2 * n - 1:
            return 0

        max_count = 0

        # 현재 대각선에서 시작 좌표 계산
        if diagonal_idx < n:
            start_y, start_x = diagonal_idx, 0
        else:
            start_y, start_x = n - 1, diagonal_idx - (n - 1)

        y, x = start_y, start_x

        # 현재 대각선 순회
        while y >= 0 and x < n:
            if mat[y][x] == 1 and not diag_used[x - y + n]:
                # 비숍 배치
                diag_used[x - y + n] = True
                count = backtrack_diagonal(diagonal_idx + 2) + 1
                max_count = max(max_count, count)
                diag_used[x - y + n] = False

            x += 1
            y -= 1

        # 현재 대각선에서 비숍을 놓지 않는 경우
        max_count = max(max_count, backtrack_diagonal(diagonal_idx + 2))

        return max_count

    # 짝수 대각선 + 홀수 대각선
    result = backtrack_diagonal(0) + backtrack_diagonal(1)
    print(result)


solution3()


def solution1():
    # 체스판을 흑백으로 분할
    black_cells = []
    white_cells = []

    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                if (i + j) % 2 == 0:  # 흑색 칸 (좌표 합이 짝수)
                    black_cells.append((j, i))  # (x, y) 형태로 저장
                else:  # 백색 칸 (좌표 합이 홀수)
                    white_cells.append((j, i))  # (x, y) 형태로 저장

    def isCanPlace(x, y, bishops):
        # 기존에 놓인 비숍들과 대각선 충돌 확인
        for bx, by in bishops:
            if abs(x - bx) == abs(y - by):  # 같은 대각선상에 있음
                return False
        return True

    def dfs(cells, idx, cnt, bishops):
        nonlocal result
        result = max(result, cnt)

        # 현재 인덱스부터 끝까지 탐색
        for i in range(idx, len(cells)):
            x, y = cells[i]

            if isCanPlace(x, y, bishops):
                bishops.append((x, y))
                dfs(cells, i + 1, cnt + 1, bishops)
                bishops.pop()

    result = 0

    # 흑색 칸에서 최대 비숍 수 계산
    dfs(black_cells, 0, 0, [])
    black_max = result

    result = 0

    # 백색 칸에서 최대 비숍 수 계산
    dfs(white_cells, 0, 0, [])
    white_max = result

    print(black_max + white_max)


# solution1()


def solution2():
    # 새로운 체스판 크기
    lim = 2 * n - 1

    # 회전된 체스판 생성
    rotated = [[0] * lim for _ in range(lim)]

    # 좌표 변환: (r,c) -> (r+c, (n-1-r)+c)
    for r in range(n):
        for c in range(n):
            if mat[r][c] == 1:
                new_r = r + c
                new_c = (n - 1 - r) + c
                rotated[new_r][new_c] = 1

    # 각 열이 사용되었는지 체크
    used_col = [False] * lim
    result = 0

    def backtrack(row, count):
        nonlocal result

        if row == lim:
            result = max(result, count)
            return

        # 현재 행에 비숍을 놓지 않는 경우
        backtrack(row + 1, count)

        # 현재 행에 비숍을 놓는 경우
        for col in range(lim):
            if rotated[row][col] == 1 and not used_col[col]:
                used_col[col] = True
                backtrack(row + 1, count + 1)
                used_col[col] = False

    backtrack(0, 0)
    print(result)


# solution2()
