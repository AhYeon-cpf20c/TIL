# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Alice', 25) # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice') # 안녕하세요, 25님! Alice살이시군요.
greet('Alice') # TypeError: greet() missing 1 required positional argument: 'age'
               # ㄴ 매개변수 수에 맞게 인자를 할당해야됨
##############################################################

# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('Bob')      # 안녕하세요, Bob님! 20살이시군요. => 함수 정의할 때 할당해준 기본값 출력됨 
greet('Char', 40) # 안녕하세요, Char님! 40살이시군요.

##############################################################

# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요. ')

greet(name = '아연', age = 17) # 안녕하세요, 아연님! 17살이시군요.
greet('아연', 17)              # 안녕하세요, 아연님! 17살이시군요.

##############################################################

# 4. Arbitrary Argument Lists
def calculate_sum(*good):      # (*) 만 붙이면 된다. 이름은 무엇이든 상관 없다.
    print(f'{good}\n{good}')   # ('S', 'M', 'L', 25) f-string 사용 가능
                               # ('S', 'M', 'L', 25)
    print(2,good)              # 2 ('S', 'M', 'L', 25)   
    print(type(good))          # <class 'tuple'>

calculate_sum('S','M','L',25)

##############################################################

# 5. Arbitrary Keyword Argument Lists
def print_info(**nice):         # (**) 만 붙이면 된다. 이름은 무엇이든 상관 없다.
    print(nice)

print_info(one = '하나', two = 2)  # {'one': '하나', 'two': 2}

##############################################################

# 인자의 모든 종류를 적용한 예시
def func(one, two, nono ='nope', *cup, **stop):
    print('하나 :', one)                    # 하나 : 1
    print('둘 :', two)                      # 둘 : 둘이다
    print('이게뭐야 :', nono)                # 이게뭐야 : 3
    print('컵 :', cup)                      # 컵 : ('그릇', '접시', '주방')
    print('멈춰 :', stop)                   # 멈춰 : {'red': '빨간불', 'green': 80}

func(1, '둘이다', 3, '그릇', '접시', '주방', red = '빨간불', green = 80)
"""
하나 : 1
둘 : 둘이다
이게뭐야 : 3
컵 : ('그릇', '접시', '주방')
멈춰 : {'red': '빨간불', 'green': 80}
"""