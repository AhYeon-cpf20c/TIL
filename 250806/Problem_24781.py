import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    delta = [0] * (N+1)
    #
    dy = [-1,1]
    dx = [-1,1]

    suma, sumb = 0
    for k in range(2,N-1):
        suma, sumb = 0, 0
        for i in dy:
            suma += arr[k+i][k]
        for j in dx:
            sumb += arr[k][k+j]
            print(sum)


# [1,1] [1,0] [1,2] [0,1] [2,1]
#     print(M)