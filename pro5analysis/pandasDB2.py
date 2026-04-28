# 원격 DB 연동 - jikwon 자료를 읽어 DataFrame에 저장
# import MySQLdb
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay from jikwon inner join buser on jikwon.busernum=buser.buserno
        """
    cursor.execute(sql)

    # for (jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay) in cursor:
    #     print(jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay)
    # DataFrame으로 출력
    df1 = pd.DataFrame(cursor.fetchall(),
                    columns=['jikwonno', 'jikwonname', 'busername', 'jikwonjik', 'jikwongen', 'jikwonpay'])
    print(df1.head(5))
    print('연봉의 총합 : ', df1['jikwonpay'].sum())
    print()
    #csv file i/0
    cursor.execute(sql)
    with open('pandasDB2.csv', mode='w', encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for row in cursor.fetchall():
            writer.writerow(row)
    
    df2 = pd.read_csv('pandasDB2.csv', header=None, names=['번호', '이름', '부서', '직급', '성별', '연봉'])
    print(df2.head(3))

    print("\n\npandas의 sql 처리 함수 이용 -----------------")
    df = pd.read_sql(sql, conn)
    print(df.head(5))
    print(df[:2])
    print(df[:-28])
    print(df['jikwonname'].count(), ' ', len(df))
    print('부서별 인원수 : ', df['busername'].value_counts())
    print('연봉 7000 이상 : ', df.loc[df['jikwonpay'] >= 7000])
    ctab = pd.crosstab(df['jikwongen'], df['jikwonjik'], margins=True)
    print('교차표\n : ', ctab)

    # 시각화
    jik_ypay = df.groupby(['jikwonjik'])['jikwonpay'].mean()     #직급별 연봉평균
    print('jik_ypay : ', jik_ypay)

    plt.pie(jik_ypay, explode=(0.2, 0, 0, 0.3, 0),
            labels=jik_ypay.index,
            shadow=True, counterclock=False)
    plt.show()
except Exception as e:
    print("처리 오류 : ", e)
finally:
    cursor.close()
    conn.close()