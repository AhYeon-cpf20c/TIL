num = int(input())
bu_hei = map(int, input().split())
case = 0
for i in range(bu_hei):
    case += 2
    for j in range(num):
        print(f'{case} {i} {j} ')



T = int(input())
for tc in range(1, T + 1):
    # 입력 및 초기화
    N = int(input())
    li = list(map(int, input().split()))

    # 로직
    result = max(li) - min(li)
    print(f'#{tc} {result}')