T = int(input())    # 테스트 케이스 수
for tc in range(1, T+1):
    H, W = map(int,input().split()) # 아파트의 세로값, 가로값
    table = [list(map(int,input().split())) for _ in range(H)]  # [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]

    DH, DW = map(int,input().split())   # 블랙리스트의 세로값, 가로값
    D_table = [list(map(int,input().split())) for _ in range(DH)]    # 블랙리스트 표


    num = [0]*100001 # 아파트 주민 index 받을 빈 리스트
    D_num = [0]*100001  # 블랙리스트 index 받을 빈 리스트

    for i in range(H):
        for j in range(W):
            number = table[i][j]
            num[number] += 1    # 아파트 주민 번호에 해당하는 index에 1씩 추가
    # print(num)
    for i in range(DH):
        for j in range(DW):
            D_number = D_table[i][j]
            D_num[D_number] += 1  # 블랙리스트 번호에 해당하는 index에 1씩 추가
    # print(D_num)
    D_count = 0
    a_count = 0
    for k in range(len(num)):
        if num[k] != 0: # 아파트에 있는 사람이 채워진 리스트
            if D_num[k] != 0:
                D_count += num[k] # 아파트 안에 있는 블랙리스트 수
            else:
                a_count += num[k] # 아파트 안에 블랙리스트가 아닌 수

    # 해당 index의 번호 뽑기 ()x-> 그걸 아파트 리스트에 index에 넣어 lst[x]
    # d_count += lst[x]z : 아파트 안에 있는 블랙리스트의 수

    print(f'#{tc} {D_count} {a_count}')



    # 주민 수를 저장할 딕셔너리
    # dat = {}


