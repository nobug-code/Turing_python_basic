'''
Data Structure
자료구조 지만 많이 사용되기 때문에 basic part에서 설명함.
선형구조

-initialiaztion
-init
a = []
a = [1, 2, 3, 4]

-Data add
append 함수를 사용
for i in range(1,101):
    a.append(i)

-check length
len(a)

-delete
del a[2]


-insert
a.insert(index, number)

-slicing
a[:3]
a[:-1]

Q. 리스트 중 최대값과 최소값을 구하가

#리스트 내포
a = [k * k for k in range(10)]

#튜플
a = (1,2,3)


한번 값을 할당 하면 바꿀수 없다. list 와 비슷하지만 메모리 측면에서 더 효율적으로 사용할 수도 있다.
'''


temp_list = [1,23,5]
prime_list = []

for i in range(len(temp_list)):

    value = temp_list[i]
    flag = 0
    for j in range(2, value):
        if(value % j == 0):
            flag = 1
    if(flag == 0):
        prime_list.append(value)

