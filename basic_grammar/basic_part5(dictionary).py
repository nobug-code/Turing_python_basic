'''
Dictionary 도 자료구조 이다.
데이터의 순서가 없는 매핑형 구조이다.
스퀸스 자료형은 데이터의 순서를 정할 수 있기 때문에 indexing이 가능하지만
매핑형은 key, value 구조에서 key 를 통해 value 값을 접근한다.

-initilization
a = {}
a = dict()
a = {'한글': 170, 'age':100, 'value': 200, 'height' : 180}

-add
a['width'] = 123

-find value
a['height']

but
value 로는 key 값을 찾지 못한다.

-key값 추출
a.keys

-value값 추출
a.values

-튜플 형태로 추출
a.items()

-값 삭제
del a['height']

-len
len(a)

하지만, diction 에서 list 로 형변환이 가능하다.
list_to_key = list(a)

아래와 같이 key 값을 숫자로도 사용할 수 있다.
d = {3:'a',2:'b',1:'c'}

list + dictionary

a = {'temper': 30, 'humidit': 10 , 'wind':4}
b = {'temper': 32, 'humidit': 12 , 'wind':4}
c = {'temper': 34, 'humidit': 13 , 'wind':4}
d = {'temper': 35, 'humidit': 14 , 'wind':4}
e = {'temper': 31, 'humidit': 15 , 'wind':4}
f = {'temper': 32, 'humidit': 16 , 'wind':4}
g = {'temper': 40, 'humidit': 20 , 'wind':4}
h = {'temper': 20, 'humidit': 7 , 'wind':4}

forecast = [a,b,c,d,e,f,g,h]

Q. 값의 어떻게 접근할까??

'''
