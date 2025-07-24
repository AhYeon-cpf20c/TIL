# 반복문 요약
# - for vs while

# for 문
# - 반복한 자료나 범위가 명확할 때 (반복 횟수가 정해져 있을 때)
# - 예) 1~10까지 출력, 리스트 순회 등

# for <변수> in <반복객체>:
#     pass

# while 문
# - 어떤 조건이 만족될 때까지 반복해야 할 때
# - 예) 비밀번호 입력, 누적 합이 특정 수를 넘기 전까지 반복

# while <표현식>:
    # pass

# 무한루프가 돈다
while True:
    # 조건문으로 반복이 중지하는 상황을 만들어 주어야 한다.
    if 표현식:
        break # break: 한 겹의 반복문을 멈춘다.

numbers = [2, 3, 4, 5, 6]

for num in numbers:
    print(num, end=' ')
    num += 5   # 원본 배열이 변하지 않는다.
print()
print(numbers)

for i in range(len(numbers)):
    print(numbers[i], end=' ')
    numbers[i] += 5  # 원본 배열이 변한다.
print()
print(numbers)


# 짝수만 출력
for i in range(len(numbers)):
    # 1. 짝수라는 조건이 만족할 때만 출력해라
    # - 조건이 간단할 때는, 만족할 때만 실행해라! 라는 방법
    if numbers[i] % 2 == 0:
        print(numbers[i], end=' ')
    # 2. 짝수라는 존거닝 만족하지 않을 때는 건너뛰어라
    if numbers[i] % 2 == 1:
        continue

print()
print(numbers)