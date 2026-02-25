# 문3) 성별 직원 현황 출력 : 성별(남/여) 단위로 직원 수와 평균 급여 출력
# 성별 직원수 평균급여
# 남 3 8500
# 여 2 7800

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        sql = 'select jikwongen as 성별, count(*) as 직원수, avg(jikwonpay) as 평균급여 from jikwon group by jikwongen'
        #print(sql)
        cursor.execute(sql)  # <-- 이거 중요한 라인임

        datas = cursor.fetchall()

        for a, b, c in datas:
            print(a,b,int(c))

    except Exception as e:
        print('err : ', e)
    finally:
        cursor.close()
        conn.close()

if __name__=='__main__':
    chulbal()

# 문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)
# 직원번호 직원명 관리 고객 수
# 1 홍길동 3
# 2 한송이 1

# import MySQLdb
# import pickle

# with open('mydb.dat', mode='rb') as obj:
#     config = pickle.load(obj)

# def chulbal():
#     try:
#         conn = MySQLdb.connect(**config)
#         cursor = conn.cursor()

#         sql = 'select jikwonno as 직원번호, jikwonname as 직원명, count(gogekno) as 관리고객수 from jikwon inner join gogek on gogekdamsano=jikwonno GROUP BY jikwonno'
        
#         cursor.execute(sql)

#         datas = cursor.fetchall()

#         for a, b, c in datas:
#             print(a,b,int(c))

#     except Exception as e:
#         print('err : ', e)
#     finally:
#         cursor.close()
#         conn.close()

# if __name__=='__main__':
#     chulbal()