import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N명의 고객 수 입력
    charge = map((int, input().split()))
    P = int(input())    #

    for i in range(P):
        req = map(int, input().split()) # 요청수 P 만큼 조정값 입력 받음
        for j in


'''
고객수 : 5
고객별 요금 : 1 2 3 4 5
요금 조정 요청 수 : 1
요금 조정 요청 가격(시작/끝/변화량) : 1 3 10

1. 델타 배열 만들기
0 0 0 0 0
delta = [0, 0, 0, 0, 0]

1 3 10 입력
delta = [0, 10, 0, 0, -10]

2. 델타 배열 활용하기
- 델타 값을 누적하면서 계산하기 위해 current_delta 변수 필요

delta = [0, 10, 0, 0, -10]
arr : 1 2 3 4 5

arr[0]단계
current_delta = 1 + 0 => 1
값 : 1 2 3 4 5

arr[1]단계
current_delta = 2 + sum(delta[:1]) => 12
값 : 1 12 3 4 5

arr[2]단계
current_delta = 3 + sum(delta[:2]) => 13 
값 : 1 12 13 4 5  

arr[3]단계
current_delta = 4 + sum(delta[:3]) => 14
값 : 1 12 13 14 5

arr[4]단계
current_delta = 5 + sum(delta[:4]) => 5
값 : 1 12 13 14 5
'''

