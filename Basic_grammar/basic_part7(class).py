'''
클래스도 자료 구조의 한 종류이다.

클래스는 새로운 자료형을 정의하는것이고,
인스턴스는 이 자료형의 객체를 생성하는 것이다.

붕어빵 틀을 클래스
인스턴스
붕어빵을 객체라고 생각하자

구조
메소드 == 함수, 변수

클래스의 특징
상속, 부모 클래스의 함수를 사용할 수 있다.

class A:
    self.a = 10
    def say(self):
        print("hi im a")


class B(A):
    def f(self):
        pass
b = B()
b.f()

pass 는 아무것도 실행 할 것이 없다는 것을 의미한다.
self 는 해당 인스턴스의 객체를 뜻한다.
__init__ 는 초기화 작업이 이뤄지는곳
정적 메소드

@staticmethod  는 클래스에 의해 정의되는 네임스페이스에 들어 있는 보통 함수
class Foo:
    @staticmethod
    def add(x,y):
        return x + y

#전역 변수 같이 사용한다.
print(Foo.add(3,6))

import , from

'''