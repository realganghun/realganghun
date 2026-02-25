# 문1) jikwon 테이블 자료 출력

# 키보드로부터 부서번호를 입력받아, 해당 부서에 직원 자료 출력

# 부서번호 입력 : _______

# 직원번호 직원명 근무지역 직급

# 1 홍길동 서울 이사

# ...

# 인원 수 :

# import MySQLdb

# config = {'host' : '127.0.0.1', 'user':'root', 'password':'123', 'database' : 'test', 'port' : 3306, 'charset' : 'utf8'}

# def chulbal():
#     try:
#         conn = MySQLdb.connect(**config)
#         cursor = conn.cursor()

#         bu_no = input('부서번호 입력 : ')
#         sql = '''
#         select jikwonno as 직원번호, jikwonname as 직원명, buserloc as 근무지역, jikwonjik as 직급 from jikwon 
#         inner join buser on busernum=buserno where busernum = {0}'''.format(bu_no)
#         #print(sql)
#         cursor.execute(sql)  # <-- 이거 중요한 라인임

#         datas = cursor.fetchall()
#         if len(datas) == 0:
#             print(bu_no + '번 부서는 없음')
#             return #sys.exit(0) <-- 함수 탈출
        
#         for jikwonno, jikwonname, buserloc, jikwonjik in datas:
#             print(jikwonno, jikwonname, buserloc, jikwonjik)

#         print('인원 수 : ', len(datas))
#     except Exception as e:
#         print('err : ', e)
#     finally:
#         cursor.close()
#         conn.close()

# if __name__=='__main__':
#     chulbal()

# 문2) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력


# 직원번호 입력 : _______

# 직원명 입력 : _______

# 직원번호 직원명 부서명 부서전화 직급 성별

# 1 홍길동 총무부 111-1111 이사 남

# ...

# import MySQLdb
# import pickle

# #config = {'host' : '127.0.0.1', 'user':'root', 'password':'123', 'database' : 'test', 'port' : 3306, 'charset' : 'utf8'}

# with open('mydb.dat', mode='rb') as obj:
#     config = pickle.load(obj)

# def chulbal():
#     try:
#         conn = MySQLdb.connect(**config)
#         cursor = conn.cursor()

#         jik_no = input('직원번호 입력 : ')
#         jik_name=input('직원명 입력 : ')
#         sql = '''
#         select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명, busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별 from jikwon 
#         inner join buser on busernum=buserno where jikwonno = %s''' %jik_no
#         #print(sql)
#         cursor.execute(sql)  # <-- 이거 중요한 라인임

#         datas = cursor.fetchall()
        
#         if len(datas) == 0:
#             print('다시 입력하세요')
#             return #sys.exit(0) <-- 함수 탈출

#         for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
#             print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)

#     except Exception as e:
#         print('err : ', e)
#     finally:
#         cursor.close()
#         conn.close()

# if __name__=='__main__':
#     chulbal()

# 문2-1) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력

# 해당 직원이 근무하는 부서 내의 직원 전부를 직급별 오름차순우로 출력. 직급이 같으면 이름별 오름차순한다.

# 직원번호 입력 : _______

# 직원명 입력 : _______

# 직원번호 직원명 부서명 부서전화 직급 성별

# 1 홍길동 총무부 111-1111 이사 남

# ...

# 직원 수 :

# 이어서 로그인한 해당 직원이 관리하는 고객 자료도 출력한다.

# 고객번호 고객명 고객전화 나이

# 1 사오정 555-5555 34

# 관리 고객 수 :

# import MySQLdb

# config = {'host' : '127.0.0.1', 'user':'root', 'password':'123', 'database' : 'test', 'port' : 3306, 'charset' : 'utf8'}

# def chulbal():
#     try:
#         conn = MySQLdb.connect(**config)
#         cursor = conn.cursor()

#         jik_no = input('직원번호 입력 : ')
#         jik_name=input('직원명 입력 : ')
#         sql = '''
#         select jikwonno as 직원번호, jikwonname as 직원명, busername as 부서명, busertel as 부서전화, jikwonjik as 직급, jikwongen as 성별 from jikwon 
#         inner join buser on busernum=buserno where jikwonno = %s''' %jik_no
#         #print(sql)
#         cursor.execute(sql)  # <-- 이거 중요한 라인임

#         datas = cursor.fetchall()
        
#         for jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen in datas:
#             print(jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen)
#         print()

#         conn2 = MySQLdb.connect(**config)
#         cursor2 = conn2.cursor()

#         sql2 = 'select * from jikwon where busernum=(select busernum from jikwon where jikwonno=%s) order by jikwonjik, jikwonname' %jik_no
#         cursor2.execute(sql2)
#         datas2 = cursor2.fetchall()
#         for data in datas2:
#             print('%s %s %s %s %s %s %s %s' %data)
        
#         print('직원수 : ', len(datas2))
#         print()

#         conn3 = MySQLdb.connect(**config)
#         cursor3 = conn3.cursor()

#         sql3 = 'select gogekno as 고객번호, gogekname as 고객명, gogektel as 고객전화, year(now()) - substr(gogekjumin,1,2) as 나이 '

#     except Exception as e:
#         print('err : ', e)
#     finally:
#         cursor.close()
#         conn.close()

# if __name__=='__main__':
#     chulbal()

# 문3) 성별 직원 현황 출력 : 성별(남/여) 단위로 직원 수와 평균 급여 출력
# 성별 직원수 평균급여
# 남 3 8500
# 여 2 7800

# import MySQLdb
# import pickle

# with open('mydb.dat', mode='rb') as obj:
#     config = pickle.load(obj)

# def chulbal():
#     try:
#         conn = MySQLdb.connect(**config)
#         cursor = conn.cursor()

#         sql = 'select jikwongen as 성별, count(*) as 직원수, avg(jikwonpay) as 평균급여 from jikwon group by jikwongen'
#         #print(sql)
#         cursor.execute(sql)  # <-- 이거 중요한 라인임

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

# 문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)
# 직원번호 직원명 관리 고객 수
# 1 홍길동 3
# 2 한송이 1

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        sql = 'select jikwonno as 직원번호, jikwonname as 직원명, count(gogekno) as 관리고객수 from jikwon inner join gogek on gogekdamsano=jikwonno GROUP BY jikwonno'
        
        cursor.execute(sql)

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