import sqlite3
import pandas as pd
from calcuate_stock import cal_stock
class NaverStockDB():

    def __init__(self):
        self.con = sqlite3.connect('/Users/namgil/PycharmProjects/naver_stock/naver_db')
        self.cursor = self.con.cursor()
        self.cal = cal_stock()

    #data를 받아서 db를 생성하는 역활
    def save_db(self, stock_number, stock_df):

        '''
        만약 디비가 존재 하지 않는다면 디비를 만들고
        디비가 존재 하면 바로 값을 넣어 주는 작업을 해준다.
        '''

        print(stock_number + " makeing db.......")

        #stock_name = "stock" + stock_number
        #stock_df.to_sql(stock_name, self.con, if_exists='append')
        self.make_table(stock_number)
        self.update_data(stock_number, stock_df)


    #DB 테이블을 만든는 역활
    def make_table(self, stock_number):
        '''
        '날짜': 'date', '종가': 'close', '전일비': 'diff',
        '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'
        이 중 close, diff, open, high, low, vloume 은 모두 int
        dod_volume 전일대비 거래량 증가량
        '''

        stock_name = "stock_" + stock_number
        # DB에 들어가는 내용 테이블 이름은 stock_number가 된다.
        table_check = "CREATE TABLE IF NOT EXISTS " + stock_name + \
                      "(date TIMESTAMP PRIMARY KEY, close  INTEGER, diff INTEGER, open INTEGER, high INTEGER," \
                      "low INTEGER, volume INTEGER, dod REAL, fiveavg REAL, tewenavg REAL)"

        self.cursor.execute(table_check)
        self.con.commit()

    #DB가 있으면 데이터만 넣어주는 역활
    def update_data(self, stock_number, stock_db):
        """
        date TEXT   PRIMARY KEY, close  int, diff int, open int, high int,low int,volume int, dod int
        """
        stock_name = "stock_" + stock_number
        total_len = 1
        #1로 바꾼다.
        for i in range (total_len):
            #teween_avg = self.cal.(stock_db[close], i)

            try:
                date = str(stock_db.ix[i]['date']).split(' ')[0]
                close = int(stock_db.ix[i]['close'])
                diff = int(stock_db.ix[i]['diff'])
                open = int(stock_db.ix[i]['open'])
                high = int(stock_db.ix[i]['high'])
                low = int(stock_db.ix[i]['low'])
                volume = int(stock_db.ix[i]['volume'])

                before_volume = int(stock_db.ix[i+1]['volume'])

                print(date)

                #print(date, close, diff, open, high, low, volume)
                #전일대비 거래비율 구하는 작업
                dod = self.cal.cal_dod_volume(before_volume, volume)
                five_avg = self.cal.cal_five_avg(stock_db['close'], i, len(stock_db))
                tween_avg = self.cal.cal_tewen_avg(stock_db['close'], i, len(stock_db))
                print("tween", tween_avg)

                self.cursor.execute("insert into {} values (:date, :close, :diff, :open, :high ,:low, :volume, :dod,  :fiveavg, :tewenavg)".format(stock_name),
                            {'date': date, 'close': close, 'diff': diff, 'open': open, 'high': high,
                             'low': low, 'volume': volume, 'dod' : dod, 'fiveavg': five_avg, 'tewenavg': tween_avg})
            except:
                pass
        self.con.commit()

    def get_data(self, stock_number):

        stock_name = "stock_" + stock_number
        df = pd.read_sql_query("SELECT * from " + stock_name, self.con)
        return df

    def end_db(self):
        #commit 은 db에 반영하는 작업이다.
        self.con.close()
