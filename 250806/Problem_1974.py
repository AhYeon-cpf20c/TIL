import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    puz = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = puz[i][j]
            if num =
