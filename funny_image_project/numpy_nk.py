'''
numpy 라는 라이브러리에 대한 설명

벡터, 행렬 등 수치 연산을 수행하는 선형대수 라이브러리 이다.

벡터 , 행렬에 대한 설명을 해야 한다.

특징

모든 배열의 값이 기본적으로 같은 타입이어야 한다.
각 차원을 축이라고 표현합니다.

ex ) 3d space [1,2,1] 같은 배열로 표현 가능, 1개의 축을 가진다.
여기서 축은 3개의 element 를 가지고 있다고 하며 length도 3

퀴즈) [[1,0,0], [0,1,2]]
의 전체 축과, 각 축의 element, length 갯수를 말해라.
'''

# 배열 생성하는 법

import numpy as np
test_a = np.array([1,2,3])

print("생성된 배열 : {}, 생성된 배열의 type : {}".format(test_a, test_a.dtype))

test_b = np.array([1.1, 1.2, 3])

print("생성된 배열 : {}, 생성된 배열의 type : {}".format(test_b, test_b.dtype))

# 잘못된 case
# test_c = np.array(1,2,3)

# 2차원 배열
test_2d = np.array([[1,2,3], [4,5,6]])
print("생성된 배열 : {}, 생성된 배열의 type : {}".format(test_2d, test_2d.dtype))

# 데이터의 타입을 정해주는법.
test_2c = np.array([[1,2,3], [4,5,6]], dtype=float)
print("생성된 배열 : {}, 생성된 배열의 type : {}".format(test_2c, test_2c.dtype))

# 다양한 np , np.zeors, np.ones, np.empty 모두다 shape을 넣어 준다.
a = np.zeros((3,4))
b = np.ones((2,2))
c = np.empty((3,3))

#  np.arange(), np.linspace() 를 이용하여 연속적인 데이터를 만들 수 있다.
# arange 는 n 만큼 차이나는 배 생성
# linsapce는 n등분 만큼의 배열 생성
a = np.arange(1, 10, 1)
print(a)

b = np.linspace(0, 1, 100)
print(b)

# reshape 데이터는 그대로 유지한채 차원을 쉽게 변경해준다.
print(b.reshape(5, 20))
