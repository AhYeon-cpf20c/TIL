i = 1
def num(n):
    if i < n:
        i += 1
        continue
    



print(i)
num(5)

def solution(n):
    total = 0
    now = 1

    while total < n:
        total += now
        now += 1
    print(f'누적 합이 {n} 이상이 된 시점 마지막 숫자 = {now-1}')

solution(10)