
c = set()
d = {}
print(type(c))
print(type(d))


a = {1, 2, 3}
b = {2, 3, 4}
print(a | b) # 합집합 - {1, 2, 3, 4} | : 엔퍼센트
print(a & b) # 교집합 - {2, 3}
print(a - b) # 차집합
print(a ^ b) # 대칭차집합 (교집합 외의 부분)

# 아래 e 와 f 는 같은 값
# set 은 순서를 신경쓰지 않는다.
e = {1, 2}
f = {2, 1}
print(e == f)  

# 비교 연산자를 통해서 부분집합 여부를 알 수 있다.
g = {1, 2}
h = {1, 2, 3, 4}

print(g < h)

# dictionary - key:value 쌍으로 저장하기 위해
# - 리스트로 저장할 수 있는 모든 데이터는 딕셔너리로 표현할 수 있다.
# -> 리스트 : 순서가 있으면 더 좋을 때
# -> 딕셔너리: 순서가 없고, key 값을 통한 조회가 많을 때

# ex) 각자 점수 저장 할 때 => 딕셔너리 사용 (이름:점수)
# ex) 만약 상위 3명을 뽑을 때 => 리스트 사용 (성적순으로 정리)

# 딕셔너리 활용 

# 초기값을 넣어주면서 선언
# - key 값은 불변 데이터만 가능 (그래서 list 는 불가능하다!)
# - key 값이 변동 -> 해시값이 변동 -> 메모리 비효율적이다!
# - 자료 구조 시간에 자세하게 다룬다.
person = {
    "name": "jay",
    "age" : 20,
    (1, 2) : "test"
}
print(person)

di = {}
di["이름"] = "jay"   # 추가 (없는 key 값)
print(di)           # {'이름': 'jay'}

di["이름"] = "kim"   # 재할당 (이미 있는 key 값)
print(di)           # {'이름': 'kim'}

key = "이름"
print(di[key])      # 특정 key 값을 통해 데이터 조회 
                    # kim

# print(di["없는 키값"])   # 없는 키 값을 조회하면 에러난다.

# 키 값이 있는지 없는지 검사 (.get)
print(di.get(key))         # 있는 키 값 : value 를 출력
print(di.get("없는 키값"))  # 없는 키 값 : None을 출력
                           # 조건문을 배우고 나면, 에러 처리를 수동으로 가능하게 한다. 


# 리스트 활용
numbers = []

numbers.append(3)  # append: 가장 뒤에 데이터를 추가
numbers.append(2)
numbers.append(1)
numbers.append(5)
print(numbers)  # [3, 2, 1, 5]

print(numbers[0])   # 3 - 가장 앞 데이터  
print(numbers[-1])  # 5 - 가장 뒤 데이터

print(numbers[0:2])  # [3, 2]
print(numbers[::2])  # [3, 1]
print(numbers[1::2]) # [2, 5]

# 데이터 삭제
numbers.pop()   # pop() : 맨 뒤의 데이터 삭제
print(numbers)  # [3, 2, 1]
numbers.pop(1)  # pop(index) : index 번째가 삭제
print(numbers)  # [3, 1]

# 불변과 가변

a = [1, 2, 3]
b = a   # 참조 복사(메모리 주소 자체가 복사)
        # 같은 객체를 가리킨다.
b[0] = 10
print(f'a = {a}')
print(f'a = {b}')
print(a is b)
print(id(a))  
print(id(b))  # 주소 동일

a = [[1, 2], [3, 4]]

# 깊은 복사
# - 메모리가 완전히 다른 곳에
# 새로운 객체를 저장하겠다.
import copy 
b = copy.deepcopy(a)
b[0][0] = 10
print(a)
print(b)
print(id(a))
print(id(b))   # 주소 상이


# 얕은 복사
# - 표지만 복사한 개념 (속 페이지는 공유)
# - 껍데기는 따로 쓰고, 속은 함께 쓰자
c = [1, [2, 3]]
d = c.copy()
print(id(c))
print(id(d))
d[0] = 10
print(c)     # [1, [2, 3]]
print(d)     # [10, [2, 3]]
print(id(c[1]))  
print(id(d[1]))  # 둘은 같은 주소
d[1][0] = 30
print(c)  # [1, [30, 3]]
print(d)  # [10, [30, 3]]
 


