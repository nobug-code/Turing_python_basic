# -*- coding: utf-8 -*-

# Data Type

# 정수,유리수, 문자

# 주석 설명
'''
여러줄을 쓸때 사용하는 주석
'''
'''
int  # 정수
float  # 소수
str  # 문자
bool  # True,False
'''
d = True

# 변수는 공간 이름이 a

print(type(d))

# +, -, * , /, %


# 형변환
#    str -> int,
#    str -> float
#    float -> int
# int(변경하고하는 숫자나 타입)

# 부동호
# > , < , ==, <=, =>, !=d

# 키보드로 부터 데이터를 입력받고 형변환 시키는 작업
x = int(input())

# 함께 해보기
# 1이면 덧셈, 2면 -, 3이면 *, 4면 / , 5면 나머지를 실행하도록

# and , or
# and 는 두 조건이 모두 참일때 실행 되는거
# or 두 조건 중 하나만 참이며는 실행이 됨

# 짝수, print('even')
# 홀수, print('odd')
# 짝수 and 10 보다 작을 때 print('three')
# 홀수 or 100 보다 작을때 print('four')

d = x % 3
'''
if(d == 0):
    print("even")
else:
    print("odd")

if(d == 0 and x < 10):
    print("three")

'''