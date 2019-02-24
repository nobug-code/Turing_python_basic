#first excel file change

#second file load

#먼저 편의를 위해 제목들의 이름을 변경시켰다.

import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv('/Users/namgil/Downloads/excel_example.csv')


#어떤 title 들을 가지고 있는지 출
print(df.head())


#숫자로 된 것들의 통계치를 출력해 준다.
#중량 이랑 TEU 가 제대로 나오지 않는다.
'''
중량은 숫자에 , 가 들어가서 숫자로 인식을 안하는 것 같고, TEU는 -가 있어서 숫자로 인식을 
못하는 것 같다. 이 부분을 수정후 다시 돌리겠다. 
'''
k = 0
temp = []

#df['Kg'].replace(1,'kkk',inplace=True)
#값을 바꿔주는 작업을 했다.
df['Kg'] = df['Kg'].map(lambda i : i.replace(',',''))

df['Kg'] = df['Kg'].map(lambda i : i.replace('-','0'))

df['Kg'] = df['Kg'].map(lambda i : int(i) if i != '0' else None)


df['TEU'] = df['TEU'].map(lambda i : i.replace('-','0'))

df['TEU'] = df['TEU'].map(lambda i : int(i.replace(',','0')))

df['TEU'] = df['TEU'].map(lambda i : int(i) if i != 0 else None)


### 변환작업 끝 !!

#값들의 평균, 같은 기본적인 연산을 해서 보여 준다.
print(df.describe())


#Null data check

#format 사용법 {}로 자리를 확보 .2f 면 소수를 {:}면 칸을 확보하는 역활을 한다.

for col in df.columns:

    msg = 'column : {:>10}\t Percent of NaN value:{:.2f}%'.format(col,100* (df[col].isnull().sum()/
                                                                            df[col].shape[0]))
    print(msg)

#시각적으로 보여주는 것 Null 데이터가 있는지 없는지를 그래프 상으로 보여준거
#msno.matrix(df = df.iloc[:,:],figsize=(10,5),color=(0.8,0.5,0.2))


'''

값이 너무 많아서 그래프가 예쁘게 나오지 않음


df['Ori'].value_counts().plot.pie(explode = None,
                                 autopct='%1.1f%%',
                                 shadow=True)
                                                
'''
#plt.show()

#데이터의 max, mean, min value 구하기

print("max value : {:.1f}".format(df['Kg'].max()))
print("min value : {:.1f}".format(df['Kg'].min()))
print("mean value : {:.1f}".format(df['Kg'].mean()))


