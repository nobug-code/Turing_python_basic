#for 문
'''
for i in range(condition):
    #코드를 적어 준다


for i in range(first,second):

    #first는 처음 숫자의 시작을 정해주고
    #second 는 마지막 숫자의 범위를 정해 준다.

    #ex)
for i in range(1,10):
    print(i)

출력
1
2
3
4
5
6
7
8
9



'''

#반복문 연습해보기 별찍기
'''
print("*")
print("*"*2)
print("*"*3)
print("****")
print("*****")

print("***")
print("**")
print("*")


#반복문을 사용해서 별찍기를 구현
for i in range(0,10):
    print("*"*i)

for i in range(10,1,-1):
    print(i)

#while문
#for 문은 고정된 범위일때 사용하기 좋고, while문은 언제 종료 될지 모를때 사용하는 것이 좋다 .

#a = input()

#while문을 for문 처럼 사용하기

i = 0
while(i < 5):

    print("hi")
    i = i + 1


문제 풀기


1. 3,6,9 문제 
    
    범위 1 ~ 100
    ex) 출력 1,,*,4,5,*,7,8,*,14,15,*

    for 문이랑 if문을 사용해서 만들기
    while문 이랑 if문을 사용해서 만들기



# break 반복문을 빠져 나간다. continue 특정 조건을 만족하면 위로 올라가서 다시 조건문을 수행시킴
while(True):

    print("Input the value :")
    a = int(input())

    b = 3
    c = 2
    if(a == 10):
        continue

    if(a == 1):
        print(c + b)

    elif(a == 2):
        print( c - b)

    else:
        print(c * b)



loop 문의 중첩



for i in range(3):

    for j in range(10):
        print("i is %d, j is %d"%(i,j))

#중첩을 이용해서 구구단을 출력해보기
# 2 ~ 9단이 출력되어야 한다.
print("%d * %d = %d"%(2,3,2*3))

#while문을 이용해서 특정 구구단만 출려하기
#a = int(input())


#비트에 대해 설명 , 컴퓨터 구조
# 2진수, 10 진법을 2진법을 바꾸기

a = 2
print(a << 2)
print(a >> 1)
'''