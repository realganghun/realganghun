# 개인용 database : SQLite3 - 파이썬에 기본 모듈로 제공
# https://www.sqlite.org
# 모바일 기기, 임베디드 시스템에 주로 사용함

import sqlite3

print(sqlite3.sqlite_version)

#conn = sqlite3.connect('exam.db')
conn = sqlite3.connect(':memory:') #RAM에만 db저장함. 일회용짜리

try:
    cur = conn.cursor() #SQL문 처리를 위한 cursor 객체 생성

    #테이블 생성
    cur.execute("create table if not exists friends(name text, phone text, addr text)") #sql문장은 큰따옴표 두르기

    #자료 입력
    cur.execute("insert into friends values('홍길동', '222-2222', '광진구 폭주족')")
    cur.execute("insert into friends values(?, ?, ?)", ('신기해', '333-3333', '광진구 맛피자')) #외부에서 정보를 입력받는 경우

    inputdatas = ('신기방기', '444-4444', '광진구 갱스터')
    cur.execute("insert into friends values(?, ?, ?)", inputdatas)
    conn.commit()

    #자료 보기
    cur.execute("select * from friends")
    print(cur.fetchone()) #fetchone : 한 개의 레코드 읽기 / fetchall : 모든 레코드 읽기
    print()
    cur.execute("select name, addr, phone from friends") #읽어오는건 내 마음!

    for r in cur:
        #print(r)
        print(r[0] + ' ' + r[1] + ' ' + r[2])

except Exception as e:
    print('err : ', e)
    conn.rollback()
finally:
    conn.close()