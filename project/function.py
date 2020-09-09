import pandas as pd
import mysql.connector
import re

config = {'user' : 'root', 'password':'cp2249cp', 'host': 'localhost', 'database':'pythondb','port':3306}

def getConn():  # MariaDB와 Python 연결
    conn =  mysql.connector.connect(**config)
    return conn



class Filters:  # 정제하는 Filter 클래스
    def filter_1(self,file):    # 2차원 배열리스트를 1차원 배열리스트 로 바꾸고 숫자와 아이디, NaN 값을 Filtering 하는 함수
        file_name = file + '.txt'
        list_1=pd.DataFrame(pd.read_csv(file_name,encoding='utf-8'))
        list_food=[]
        list_2=list_1.fillna(0) #nan을 0 으로

        for i in range(1,list_1.shape[0]):
            for j in range(2,30) :
                if list_2.iloc[i,j] == 0:
                    pass
                else:
                    list_food.append(list_2.iloc[i,j])

        return list_food

    def filter_2(self,file):     # 한글과 영문 대/소문자, 숫자를 제외한 값을 Filtering 하는 함수
        list_food=Filters.filter_1(0,file)
        key = re.compile('[ㄱ-ㅎ|가-힣|a-z|A-Z|0-9|]+')
        list_food_str = str(list_food)
        result = key.findall(list_food_str)
        return result

class MariaDb:      # MariaDB에 저장하기위해 사용되는 sql구문을 함수를 가지는 클래스
    def create(self,name):      # 테이블 생성하는 함수
        conn = getConn()
        cur = conn.cursor()
        cur.execute('''CREATE table {}(카페 varchar(100), 공방 varchar(100), 호텔 varchar(100), 맛집 varchar(100))'''.format(name))
        conn.commit()
        conn.close()
    def insert_all(self,name,val1):     # 각 칼럼에 값을 삽입하는 함수
        conn = getConn()
        cursor = conn.cursor()
        ins_query = 'INSERT into {} values(%s,%s,%s,%s)'.format(name)
        cursor.execute(ins_query,val1)
        conn.commit()
        conn.close()

class Array:    # 각각의 1차원 배열의 리스트를 받아서 2차원 배열 리스트로 합치는 함수를 가진 클래스
    def value(self,file1,file2,file3,file4):    # 각각의 1차원 배열의 리스트를 받아서 2차원 배열 리스트로 합치는 함수
        list_instacaffe=Filters.filter_2(0,file1)
        list_instagongbang=Filters.filter_2(0,file2)
        list_instahotal=Filters.filter_2(0,file3)
        list_instafood=Filters.filter_2(0,file4)

        list_instahotal_len=len(list_instahotal)
        list_instacaffe_len=len(list_instacaffe)
        list_instagongbang_len=len(list_instagongbang)
        list_instafood_len=len(list_instafood)

        list_con = [len(list_instahotal),len(list_instacaffe),len(list_instagongbang),len(list_instafood)]
        # print(list_deagu)
        list_con = sorted(list_con)
        # print(list_deagu)

        list_all = []
        food_value = ''
        hotel_value = ''
        caffe_value = ''
        gongbang_value = ''
        for i in range(list_con[3]):
            if i >= list_instagongbang_len:
                gongbang_value = '0'
            else :
                gongbang_value = list_instagongbang[i]
            if i >= list_instahotal_len:
                hotel_value = '0'
            else :
                hotel_value = list_instahotal[i]
            if i >= list_instacaffe_len:
                caffe_value = '0'
            else :
                caffe_value = list_instacaffe[i]
            if i >= list_instafood_len:
                food_value = '0'
            else :
                food_value = list_instafood[i]
            list_all.append([caffe_value,gongbang_value,hotel_value,food_value])
        return list_all
# print(list_all)

# MariaDb.create(0,'대구')

# list_all=Array.value(0,'대구카페추천','대구공방추천','대구호텔추천','instafood')

# df=pd.DataFrame(list_all)
# df.to_csv('Deagu.csv',encoding='euc-kr')

# for i in range(len(list_all)):
#     MariaDb.insert_all(0,'대구',tuple(list_all[i]))

