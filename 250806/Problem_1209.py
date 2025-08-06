import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):

    # 100 x 100 2차원 배열
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_max = 0

    # 각 행의 합
    for i in range(100):
        current_sum = 0
        for j in range(100):
            current_sum += arr[i][j]
        if sum_max < current_sum:
            sum_max = current_sum
    # 각 열의 합
    for i in range(100):
        current_sum = 0
        for j in range(100):
            current_sum += arr[j][i]
        if sum_max < current_sum:
            sum_max = current_sum

    # 좌상단 대각선의 합
    x_sum = 0
    for i in range(100):
        x_sum += arr[i][i]
    if sum_max < x_sum:
        sum_max = x_sum

    # 좌하단 대각선의 합
    x_sum = 0
    for i in range(100):
        current_sum += arr[99-i][i]
    if sum_max < x_sum:
        sum_max = x_sum

    print(f'#{tc} {sum_max}')

