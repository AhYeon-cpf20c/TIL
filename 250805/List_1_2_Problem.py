# 매 번 입력 붙여넣기가 힘드니, 파일에서 입력을 받아오는 방식
import sys
sys.stdin = open("input.txt")

T = int(input()) # 테스트 케이스 입력
for tc in range(1, T + 1): # 테스트 케이스 순회
    N = int(input()) # 노선의 개수

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int,input().split()) # 타입 = int
        # A ~ B번째 사이의 정류장을 운영함
        for j in range(A, B + 1):
            bus_stop[j] += 1  # A 부터 B 까지의 정류장 번호를 리스트에 인덱스 각인 bus_stop[j] += 1
    P = int(input())
    c_list = []
    # P개의 정류장 번호가 입력됨 -> 각 정류장을 지나는 버스 노선 구하기
    for _ in range(P):
        c = int(input())
        c_list.append(bus_stop[c]) # 빈 리스트에 C번 버스 정류장 번호를 추가

    print(f'#{tc}',*c_list)












# P = 5 # 버스 정류장 개수
# Cj = 1 2 3 4 5 # 버스 정류장 번호
# A1 = O O O X X # A1 버스가 다니는 정류장 노선
# A2 = X O O O O # A2 버스가 다니는 정류장 노선
# --> 각각 Cj번 버스 정류장을 지나는 버스 노선의 개수는?




    # box 리스트에 상자 높이에 맞춰 index 담기
    # box[i] = num
    # box_list[num] += 1

    # 최고 박스에서 최저 박스로 1개씩 이동
    # -> 최저 박스가 2번째 최저 박스 따라잡을 때까지
    # -> 최고 박스가