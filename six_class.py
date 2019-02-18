#function 함수

'''

파이썬 코드 위에서 부터 아래로 가면서 코드가 실행이 되
함수는 코드 들의 집합, 입력값, 출력값이 있어서
특별한 기능을 수행하도록 코드들의 모임이다.

복잡한 내용을 추상화 시켜서 프로그램을 편리하게 해준다.

'''

def test_kk():

    #코드
    a = 3
    b = 4

    c = a + b
    print(c)

    return

def add(a,c):

    d = a + c



#input 을 하나 받고 1이면 덧셉, 2면 뺄셈, 3면 곱셈, 4면 나눗셈을 수ㅇ행 ,
# 두 개를 입력 받는다 .

def nk_test(a,*args):

    print(a,args)


#call by value
#call by reference
#call by object reference

x = 7

def test():

    x = 3


    def kkkk():


        print(x)


    kkkk()


test()


lambda x,y : x + y

def nam(func):

    return [func(x) for x in range(-10,10)]

print(nam(lambda x: x * x))




