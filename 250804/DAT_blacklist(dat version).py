T = int(input())


for tc in range(1, T + 1):
    H, W = map(int, input().split())

    # 아파트 기준으로 dat 를 만든다.
    dat = [0] * 100001
    for _ in range(H):
        row = list(map(int, input().split()))
        for num in row:
            dat[num] += 1

    blacklist_count = 0
    BH, BW = map(int, input().split())
    for _ in range(BH):
        row = list(map(int, input().split()))
        for num in row:
            blacklist_count += dat[num]
            dat[num] = 0  # 중복계산 방지용

    normal_count = (H * W) - blacklist_count
    print(f'#{tc} {blacklist_count} {normal_count}')