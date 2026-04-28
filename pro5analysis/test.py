# import numpy as np
# data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(data[:, ::-1][::-1])

# 실행결과 :
# [[16 15 14 13]
# [12 11 10  9]
# [ 8  7  6  5]
# [ 4  3  2  1]]

# DataFrame(np.arange(12).reshape((__, __)), _______=[              ],  _______ = [            ])
# import pandas as pd

# df = pd.DataFrame(np.arange(12).reshape(4, 3), index=['1월', '2월', '3월', '4월'],  columns = ['강남', '강북', '서초'])
# print(df)
# 강남 강북 서초
# 1월 0 1 2
# 2월 3 4 5
# 3월 6 7 8
# 4월 9 10 11
# (배점:5)

# from pandas import DataFrame
# frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']}, index=['a','b', 'c','d'])
# print(frame.T)
# frame2 = frame.drop('d')    # 인덱스가 'd'인 행 삭제
# print(frame2)

# 실행결과 1 :
#         a  b  c  d
# bun    1  2  3  4
# irum  aa  bb  cc  dd

# 실행결과 2 :
#   bun irum
# a    1  aa
# b    2  bb
# c    3  cc

# data = {
#     'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
#     'inwon':[23, 25, 15]
# }
# df3 = DataFrame(data)

# results = pd.Series([x.split()[0] for x in df3.juso])
# print(results)



# [문항11] MariaDb에 저장된 jikwon 테이블을 사용한다. 담당 고객이 없는 직원의 수, 연봉 평균, 표준편차를 출력하는 프로그램을 작성하려고 한다.

# 조건 :
# 1) DB의 자료를 SQL문으로 읽어, DataFrame에 저장한다.
# 2) 아래의 main() 함수에 적당한 코드를 완성하시오.
# (배점:10)
import MySQLdb
import pandas as pd
import numpy as np
import sys

def main():
    CONFIG = {"host": "127.0.0.1", "user": "root", "passwd": "123", "db": "test", "port": 3306, "charset": "utf8" }

    sql = """
    SELECT jikwonname, jikwonpay, gogekno, gogekname FROM jikwon LEFT OUTER JOIN gogek ON jikwonno = gogekdamsano
    """
    conn = MySQLdb.connect(**CONFIG)
    cursor = conn.cursor()
    cursor.execute(sql)

    df_gogek = pd.DataFrame(cursor.fetchall(), 
                        columns=['직원명', '연봉', '고객번호', '고객명'])
    print(df_gogek)

    no_gogek_df = df_gogek[df_gogek['고객번호'].isnull()]
    print(no_gogek_df)
    count = len(no_gogek_df)
    pay_mean = no_gogek_df['연봉'].mean()
    pay_std = no_gogek_df['연봉'].std()

    print("인원수 : ", count)
    print("연봉 평균 : ", pay_mean)
    print("표준편차 : ", pay_std)

    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()

# datas = np.random.randn(9,4)
# df = DataFrame(datas, columns=['가격1', '가격2', '가격3', '가격4'])
# print(df)
# print(df.mean(axis=0))
# print('-------------------13번------------------------')
# from pandas import DataFrame
# data = {"a": [80, 90, 70, 30], "b": [90, 70, 60, 40], "c": [90, 60, 80, 70]}

# df = DataFrame(data)
# df.columns = ['국어', '영어', '수학']
# print(df['수학'])

# print(df['수학'].std())

# print(df[['국어', '영어']])
# print('--------------------- 14번 -----------------')
# import matplotlib.pyplot as plt

# data = np.random.normal(loc = 0, scale = 1, size = 1000)
# plt.figure()
# plt.hist(data, bins=20, alpha=0.7)
# plt.title('good')
# plt.show()

# data = pd.read_csv("sales_data.csv", encoding='utf-8')
# df = DataFrame(data)
# df_pivot = df.pivot_table(index='날짜', values='제품')
# print(df_pivot)