'''
#dictionary
데이터의 순서를 정할 수 없는 매핑형이다.
스퀸스 자료형은 데이터의 순서를 정할 수 있기 때문에 indexing 이 가능하지만
매핑형은 key 를 이용해 value 값을 접근한다.

문법
{} 를 사용한다.

'''
#수업을 나가기 전에 소수 구하는 프로그램 부터 구하고 진도를 나가자

#a = {}, a = dict()

a = {'height': 170, 'age':100, 'value': 200}
#위에서 설명한 것처럼 key 값을 토대로 value 를 찾는 형태 이다.
print(a['height'])

#value 로는 key 값을 찾지 못한다.
#print(a[186])

#순서의 의해서가 아니라 키에 의해서 값을 추출한다.
#하지만 때로는 기존의 자료형으로 처리하는 것이 필요할 수 있기 때문에
#형변환이 가능하다.

#값의 추출

#key 값들만 추출
print(a.keys())
b = a.keys()

#value 값들만 추출
print(a.values())

#튜플 형태로 가져 추출

c = a.items()
print(c)

#형변환

list_to_key = list(a)
#key 값들만 변경이됨

print(list_to_key)

list_to_value = list(a.values())

print(list_to_value)

#삭제시

del a['height']

print(a)

#하지만 index은 가능하지 않다 !!
#다음 과 같이 변경이 가능하다.
a['height'] = 130

print(a)

#길이를 재는 방법
print(len(a))

#다음과 같이 사용할 수 도 있다.
d = {3:'a',2:'b',1:'c'}
print(d[1])

#활용법 (list를 이용해서 dictionary를 저장하는 방법)

a = {'temper': 30, 'humidit': 10 , 'wind':4}
b = {'temper': 32, 'humidit': 12 , 'wind':4}
c = {'temper': 34, 'humidit': 13 , 'wind':4}
d = {'temper': 35, 'humidit': 14 , 'wind':4}
e = {'temper': 31, 'humidit': 15 , 'wind':4}
f = {'temper': 32, 'humidit': 16 , 'wind':4}
g = {'temper': 40, 'humidit': 20 , 'wind':4}
h = {'temper': 20, 'humidit': 7 , 'wind':4}

forecast = [a,b,c,d,e,f,g,h]

print(forecast)

