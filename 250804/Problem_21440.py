T = int(input()) # 테스트 케이스 수
for tc in range(1, T + 1):
    n, m = map(int, input().split())    # n: 정수의 개수, m:구간의 개수
    num = list(map(int, input().split()))
    sum = 0
    sum_list = []
    for i in range (0,(n-m)+1): # 주어진 n개의 숫자를 이웃한 m개씩 더함
        for j in range(i,i+m):
            sum += num[j]    # 이웃한 m개의 숫자끼리의 총 합
            print(sum)
        sum_list.append(sum)
    # print(sum_list) # [3, 9, 18, 30, 45, 63, 84, 108]

    max_sum = sum_list[0]
    for i in range(1, len(sum_list)):
        if max_sum < sum_list[i]:
            max_sum = sum_list[i]
        else:
            continue
    min_sum = sum_list[0]
    print(max_sum)
    for j in range(1, len(sum_list)):
        if min_sum > sum_list[i]:
            min_sum = sum_list[i]
        else:
            continue
    print(min_sum)
    result = max_sum - min_sum # 가장 큰 경우 - 가장 작은 경우
    print(f'#{tc} {result}')
