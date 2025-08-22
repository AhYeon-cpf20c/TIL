import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input()) + 1):
    N = int(input())
    P = list(map(int, input().split()))

    total = N-1
    for i in range(len(P)):
        if P[i] != 0:
            total += 1
            total += ((i+1)-P[i])

    print(f'#{tc} {total}')