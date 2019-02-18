#list

a = []

#list 라는 데이터 타입이 있다.
print(type(a))

a = [1,2,3,4,5,6]

print(a)

a = []

a.append(1)
a.append(2)

print(a)

# 1 부터 10까지 list 의 값을 대입 for, while 문을 사용해서
a = []

for i in range(1,11):

    a.append(i)

import random

a = [1, 2, 3, 4, 5, 6, 7]

print(a)

#원소에 접근하는 방
#print(a[4][0])

#길이

print(len(a))

for i in range(len(a)):

    print(a[i])

i = 0

while(i < 5):

    print(a[i])
    i = i + 1

# 리스트 원소중 최대값, 최소값을 구하기 !

a = [10,3,4,10000000,1]


b = 0

for i in range(len(a)):

    if(b < a[i]):

        b = a[i]

#삭제
del a[3]

print(a)

#삽입
a.insert(3,10000)

print(a)

#슬라이싱
print(a[:3])


#리스트 내포
b = []
for i in range(10):
    b.append(i * i)

a = [k * k for k in range(10)]


print(a + a)


#튜플
a = (1,2,3)


