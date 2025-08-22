import sys
sys.stdin = open("input.txt")
# 학번 : 1444221

for tc in range(1, int(input()) + 1):
    N = int(input())
    P = list(map(int, input().split()))

    # print(p.index(p[-1]))
    # 1 번 방은 포탈 1개 -> 무조건 2번방 이동
    # 2 ~ N-1 번방 까지 처음은 무조건 왼쪽(왼쪽방 중 아무곳이나 가능한듯) / 두번째는 오른쪽
    # 각 자리마다 p[i] 번호가 주어지는데 왼쪽포탈로 이동시 i 번째 자리로 이동하면 된다.
    # 마지막 방 도착하면 끝

    # 인덱스로 다시 정리하는게 나을듯
    # lst = []
    # # [1, 2, 3, 4, 5]
    # for i in range(1, len(P)+1):
    #     lst.append(i)
    # print(lst)

    # for j in range(1, N):
    #
    #     # p[i] 숫자 빼오기
    #     for a, b in zip(lst, P):
    #
    #     if j == 1:
    #         cnt += 1
    #     for p in P:
    #
    #
    # cnt = 0
    # # 들어가는 방이 마지막 방의 인덱스번호와 같아지면 반복문 종료
    # a = 1
    # while a != lst[-1]:
    #     if a == lst[0]:
    #         cnt += 1
    # P = [0, 1, 1, 2, 0]
    lst = [0] * (N+1)
    # 마지막 인덱스 값이 증가되면 종료
    i = 0
    while True:
        # 첫 방 입장 -> 다음 방 이동 -> 첫 방 돌아오기
        if P[i] == 0:
            if lst[0] == 0:
                i += 1
            elif lst[i] != 0:
                i += 1
                lst[i] += 1
            # lst[i] += 1
        # elif lst[0] != 0:
        #     i += 1
        #     lst[i] += 1

        elif lst[i] != 0 and P[i] != 0:
            lst[i] += 1
            i += 1
        # 다음방의 인덱스 값이 '0'이라면 index[i]로 이동
        elif P[i] != 0 and lst[i] == 0:
            if lst[i] == 0:
                lst[i] += 1
                i = P[i] - 1
        # 탈출
        if i >= len(P) or lst[-1] != 0:
            break
    print(lst)
    total = 0
    for a in lst:
        total += a

    print(f'#{tc} {total}')



