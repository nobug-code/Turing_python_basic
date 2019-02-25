#class
'''
클래스는 새로운 자료형을 만드는것 , 인스턴스는 이 자료형의 객체를 생성하는 거다.

만들어지는게 인스턴스라고 생각을 하고 - 붕어빵
틀을 클래스라고 생각하면 된다.

특징

상속

상속받는 클래스
말그대로 상위 클래스에 대한 것을 밑에 클래스가 사용을 하는 것

class A:

    def say(self):
        print("hi im a")

class B(A):

    pass

pass 는 아무것도 실행 할 것이 없다는 것을 의미한다.



b = B()
b.f()


self 는 해당 인스턴스의 객체를 뜻한다.

__init__ 는 초기화 작업이 이뤄지는곳

정적 메소드

@staticmethod  는 클래스에 의해 정의되는 네임스페이스에 들어 있는 보통 함수

'''

class Foo:

    @staticmethod
    def add(x,y):
        return x + y

#전역 변수 같이 사용한다. 

print(Foo.add(3,6))





class test: # Header
    pass # Body


