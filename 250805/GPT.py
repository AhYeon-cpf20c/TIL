import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    bus_stop = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            bus_stop[i] += 1

    P = int(input())
    c_list = []

    for _ in range(P):
        c = int(input())
        c_list.append(bus_stop[c])  # 바로 조회해서 append

    print(f'#{tc}', *c_list)