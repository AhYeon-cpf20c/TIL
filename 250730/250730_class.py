# class 라는 것을 왜 쓸까?
# - 중복된 코드를 많이 줄일 수 있다.

# 전사, 궁수, 마법사
# - 공통: 체력, 마나, 공격력
# - 기능: 공격하기, 걷기, 상태확인
# 전사만 할 수 있는 것: 칼로때리기(), 강하게 소리지르기()
# 궁수만 할 수 있는 것: 활쏘기(), 자세히 살펴보기()
# 마법사만 할 수 있는 것: 마법쓰기(), 똑똑해지기()

# 상황1. 전체 캐릭터의 수를 관리해야 한다.
# - 전역변수로 관리
#       -> Character class 와 관련된 변수인데, 외부에 값을 관리
#       --> 유지보수가 어려워진다. 

class character:
    total_players = 0 # 클래스 변수
                      # 모든 인스턴스가 공유하는 값
    # self : 인스턴스 자기자신을 가리킨다.
    # 생성자에 전달되는 값 : 인스턴스의 초기값
    def __init__(self, hp, mp, power):
        # 초기화
        self.hp = hp # <- hp는 다른 이름으로 변경가능하나 일반적으로 변수와 동일하게 사용함
        self.mp = mp
        self.power = power

        character.total_players += 1
    
    # 인스턴스 메서드 (인스턴스마다 공격력이 다름)
    def attack(self): # self 안써주면 버그난다. 인스턴스가 자기꺼가 아니라서 접근이 안됨
        print(f"{self.power}의 데미지로 공격!") 
        # 10의 데미지로 공격!
        # 100의 데미지로 공격!
total_players = 0
# 클래스명() => 클래스의 생성자를 호출해라고 정해놓음

# 인스턴스는 각자 값이 다르다.
character1 = character(100, 50, 10) # 1번 캐릭터 (인스턴스)
character2 = character(500, 200, 100)   # 2번 캐릭터 (인스턴스)

character1.attack()
character2.attack()

# 인스턴스를 통해서도 클래스 변수에 접근 가능!

# print(f'전체 캐릭터 수 = {character1.total_players}')
# ㄴ--> 이렇게 하지마라! 
print(f'전체 캐릭터 수 = {character.total_players}') # 전체 캐릭터 수 = 2

class Warrior(character): # -> 상속 : 부모 클래스의 내용을 가져온다.
    pass

warrior1 = Warrior(200, 10, 90)
print(warrior1.hp, warrior1.mp) # 200 10