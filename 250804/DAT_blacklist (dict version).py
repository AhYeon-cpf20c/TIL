T = int(input())


for tc in range(1, T + 1):
    H, W = map(int, input().split())

    # 주민 수를 저장할 딕셔너리
    dat = {}

    for _ in range(H):
        row = list(map(int, input().split()))
        for num in row:
            # num 이라는 key가 없으면 value를 1으로 생성
            # num 이라는 key가 있다면, 기존 value 에 + 1
            dat[num] = dat.get(num, 0) + 1

    blacklist_count = 0

    BH, BW = map(int, input().split())
    for _ in range(BH):
        row = list(map(int, input().split()))
        for num in row:
            if dat.get(num):
                blacklist_count += dat[num]
                dat[num] = 0  # 중복 방지용

    normal_count = (H * W) - blacklist_count
    print(f'#{tc} {blacklist_count} {normal_count}')