T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(H)]

    dat = [0] * 10000001

    max_count = 0
    max_index = 10000000

    for i in range(H):
        for j in range(W):
            number = table[i][j]
            dat[number] += 1

            # 더 많이 출근한 경우 해당 count 와 index 가 정답
            if max_count < dat[number]:
                max_count = dat[number]
                max_index = number

            # 만약 count 가 동일하다면, index 를 기준으로 더 작은 index 가 정답
            if dat[max_index] == max_count and number < max_index:
                max_index = number

    print(f'#{tc} {max_index}')
