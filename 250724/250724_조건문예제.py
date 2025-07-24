# def step1(one):
#     if one >= 140:
#         print('탑승 가능합니다.')
#     else:
#         print('탑승 불가입니다.')

# step1(20)

# print(True and False) # False
# print(True or False)  # True

# def step2(age, cm):
#     # 두 조건을 모두 만족해야만, 탑승 가능
#     if age >= 12 and cm >= 140:
#         print('탑승 가능합니다.')
#     else:
#         print('탑승 불가입니다.')
# step2(11,150)

def step3(age, cm, family):
    if cm >= 140 and age >= 12:
        print('탑승 가능 (단독)')
    elif cm >= 140 and age < 12:
        if family == 'n':
            print('탑승 불가')
        else:
            print('혼자서는 탑승 불가 (보호자동반)')
    else:
        print('키 제한으로 탑승 불가')

step3(12,120,'y')







    
    
