'''
function 이란???
코드들의 집합니다. 단순히, 코드들의 집합이 아니라 특별한 기능들을 수행하는 코드들의 모임이다.
함수의 장점으로는 반복적으로 사용가능하고, 논리적으로 프로그램 하는데 큰 이점이 있다. 복잡한 내용을 추상화 시켜 프로그램을 편리하게 해 준다.

문법
def 함수이름(인자):
    코드
    return 값
의 형태를 취한다.

Q. 소수를 구하는 함수를 만들어라

return 값을 안써도 자동으로 반환이 된다.
어떤 값이 return 되는가???

- None 이란 ? 파이썬 내장 객체로서 아무것도 없다는 것을 표현하는 객체이다.

call by value, c
call by refernce, java 가 있다.
value에 의한 참조는 값의 복사, refence 는 주소값을 참조한다.
파이썬은 call by object reference 방법을 사용한다.

def f(t):
    t = [3,4,5]
    return t
a = [1,2,3]
a = f(a)
print(a)
- int,str -> 값 자체를 변경할 수 없기 때문에 값을 복사해서
f(a)
print("a is ",a)

- 새로운 객체를 참조 했기 때문에 값이 변경되지 않는다.
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

- 변수의 이름은 항상 안쪽에서부터 바깥쪽을 찾아 나간다.
    x = 7
    def test():
        x = 3
        print(x)
test()

-입력값
def area(height, width):
    print(height* width)
area(20,width=10)
#인자를 몇개 받을지 모를때 사용하면 나머지는
def nk_test(a,*args):
    print(a,args)
nk_test(1)
nk_test(2,3)
nk_test(2,3,4,5,6)

-람다함수
이름이 없는 한줄 짜리 함수 이다.
정의와 함께 동시에 사용가능해서 편리하다.
lambda : 1
def nam(func):
    return [func(x) for x in range(-10,10)]
def k(func):
    return func(2,1)
print(k(lambda  x,y : x + y))
print(nam(lambda x : x * x))

'''









