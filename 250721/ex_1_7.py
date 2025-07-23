# 원주율
P = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
R = 15

pi = '원주율 : '
radius = '반지름 : '
round = '원의 둘레 : '
dim = '원의 넓이 : '

round_result = 2 * P * R
dim_result = P * (R**2)

print (pi, f"{P:.15f}")                    # 원주율 
print (radius, R)                          # 반지름
print (round, f"{round_result:.14f}")      # 원의 둘레 : 2*pi*r
print (dim, f"{dim_result:.13f}")          # 원의 넓이 : pi*r^2



