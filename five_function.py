'''
함수는 코드들의 집합이다.

지금 까지 우리가 배운 코드는 위에서 부터 아래로 실행 되는 형태이다.
함수는 코드들의 집합으로써 하나의 실행 단위이다. 특별한 기능들을 수행을 담당하는 코드들의 모임이다.
반복적으로 수행이 가능하고, 논리적으로 프로그래밍하는데 큰 이점이 있다.
복잡한 내용을 추상화 시켜 프로그램을 편리하게 해 준다.


'''

#함수의 문법
'''
def 함수이름(인수):
    코드
    
    return 값 
    
형태를 취한다. 
'''

#지금 해봐야 할것
#입력에 따른 계산기를 만들고 이를 함수화 시키는 것

#return
'''
return 을 안써도 값이 반환이 된다. 
이번에는 print return 을 해봐서 어떤 값이 나오는지 체크해보자 

None 이란 ? 파이썬 내장 객체로서 아무것도 없다는 것을 표현하는 객체이다. 

return 

리턴 없이 종료 시켜 보자 

return 의 여러값을 넣어서 반환 시켜 보자 

'''
'''
call by value
call by refernce 

가 있는데 value에 의한 참조는 주로 값을 변경시키지 않고
referecne 는 주소값을 참조 함으로 값이 변경된다. 

하지만 파이썬에는 call by object reference 라는 특이한 방식을 사용한다. 

'''

def f(t):
    t = 10

a = 20

print(a)

#새로운 객체를 참조 했기 때문에 값이 변경되지 않는다.

def h(t):
    t = (1,2,3)

a = (5,6,7)

h(a)

print(a)


def g(t):

    t[1] = 10

a = [1,2,3]

g(a)

print(a)

def gg(t):

    t = [1,2,3]

a = [5,6,7]
gg(a)

print(a)

#변수의 이름은 항상 안쪽에서부터 바깥쪽을 찾아 나간다.
#규칙은 안쪽에서 부터 바깥쪽의 변수를 찾는거다
x = 7

def test():

    x = 3
    print(x)

test()

#입력값

def area(height, width):

    print(height* width)

area(20,width=10)

#인자를 몇개 받을지 모를때 사용하면 나머지는
def nk_test(a,*args):

    print(a,args)


nk_test(1)
nk_test(2,3)
nk_test(2,3,4,5,6)

#람다 함수
'''
이름이 없는 한줄 짜리 함수 이다. 
정의와 함께 동시에 사용가능해서 편리하다. 
'''

lambda : 1


lambda x,y : x + y

def nam(func):

    return [func(x) for x in range(-10,10)]

print(nam(lambda x : x * x))
