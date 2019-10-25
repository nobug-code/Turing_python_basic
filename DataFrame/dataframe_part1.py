#-*-coding:utf-8-*-
import pandas as pd

excel_file = 'part_time.csv'
df = pd.read_csv(excel_file)

df['total_time'] =  df['End_time'] - df['Start_time']
df['time_of_make'] = df['Make']/df['total_time']

df = df.sort_values(by=['time_of_make'], ascending=False)
df.to_csv('df.csv')

'''
import pandas as pd

#load excel file
excel_file ='movies.csv'
movies = pd.read_csv(excel_file)

#결측치를 바꿔주고 싶을때
print(movies.fillna(value=0))

#데이터의 갯수를 세고 싶을떄
print(movies['Year'].value_counts())

#열, 행 두개를 섞어서 사용하는
#print(movies.loc[10:40, ['Year', 'Title']])
#print(movies.iloc[10:40, 0:2])


#처음 단의 자료와 colum 들을 보여 준다.
print(movies.head())

#마지막 단의 자료와 column 들을 보여 준다.
print(movies.tail())

#sample 안의 수대로 랜덤하게 뽑아서 보여 준다.
print(movies.sample(5))

#column 을 확인하는 명령어
print(movies.columns)

#기본적인 통계적인 수치를 계산해서 보여준다.
print(movies.describe())

#열 범위를 부분적으로 가져 오고 싶을때
sheet_1 = movies[['Title','Year']]
print(sheet_1)

#행 범위로 부분적으로 가져 오고 싶을때
print(movies[0:10])

#열, 행 두개를 섞어서 사용하는 
print(movies.loc[0:5,['Year', 'Title']])
print(movies.iloc[3:5,0:2])

#조건으로 검색하고 싶을때
print(movies[movies.Year > 1800])

#데이터 추가 하고 싶을때 대신 (길이를 맞춰줘야 한다.)
df2 = movies[0:6].copy()
df2['E'] = ['one', 'one','two','three','four','three']
print(df2)

title = movies.Title
print(title)

year = movies.Year
print(year)

# 없는 데이터가 얼마만큼이나 있는지 구하는 것
for col in movies.columns:
    msg = print('column : {:>10}\t Percent of NaN value:{:.2f}%'.format(col,100* (movies[col].isnull().sum()/
                                                                            movies[col].shape[0])))
#결측치를 바꿔주고 싶을때
print(movies.fillna(value=0))

#데이터의 갯수를 세고 싶을떄
print(movies['Year'].value_counts())

#파일을 불러와서 계산 하고 저장하기
excel_file = 'part_time.csv'
df = pd.read_csv(excel_file)

print(df)
# 띄어쓰기가 들어 가면 에러가 난다.

df['total_time'] = df['End_time'] - df['Start_time']
print(df)

df['time_make'] = df['Make']/ df['total_time']

df = df.sort_values(by=['time_make'], ascending=False)

df.to_csv('new_time.csv')


#합치는 방
left = pd.DataFrame({'key': ['foo', 'zoo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'zoo'], 'lval': [2, 1]})
merged = pd.merge(left, right, on='lval')
print(left)
print(right)
print(merged)

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
#    key  lval
# 0  foo     1
# 1  bar     2

right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
#    key  rval
# 0  foo     4
# 1  bar     5

merged = pd.merge(left, right, on='key')
#    key  lval  rval
# 0  foo     1     4
# 1  bar     2     5
merged.to_csv('hi.csv')
'''