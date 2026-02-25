
-- --------------------------------------------------------2.11--------------------------------------------------------------------
CREATE TABLE dept(NO INT PRIMARY KEY, NAME VARCHAR(10), tel VARCHAR(15), inwon INT, addr TEXT); -- TABLE 생성, NO에 primary key를 줌

--자료 추가
#insert into 테이블명 (칼럼명, .... ) values(입력자료,...)
INSERT INTO dept(NO, NAME, tel, inwon, addr) VALUES(1,'인사과','111-1111',3,'삼성동'); --큰 따옴표는 안됨!
INSERT INTO dept VALUES(2,'영업과', '111-2222',5,'서초동');
INSERT INTO dept (NO, NAME) VALUES(3,'자재과');
INSERT INTO dept(NO, addr, tel, NAME) VALUES(4,'역삼2동', '111-5555', '영업과');

INSERT INTO dept VALUES(5, '판매과'); -- err : 입력자료와 칼럼 갯수 불일치.
INSERT INTO dept(NAME, tel) VALUES('판매과2', '111-6666'); -- err NO:pk, 생략 불가
INSERT INTO dept(NO, NAME) VALUES(5, '판매과부서는 어쩌구저쩌구 지예아 나는 다채로운 래핑과 라이밍 혹은 혼을 쏙빼놓는 랩스킬로'); -- name이 너무 길어져서 err발생

SELECT * FROM dept;
SELECT * FROM dept WHERE NO=1;

-- 자료 수정
-- update 테이블명 set 수정칼럼명=수정값,...NO. where 조건 <== 수정 대상 칼럼을 지정해서 수정함
-- primary key(pk) 칼럼의 자료는 수정대상에서 제외
UPDATE dept SET tel='123-4567' WHERE NO=2;
UPDATE dept SET addr='압구정동33', inwon=7, tel='777-8888' WHERE NO=3;

SELECT * FROM dept;

-- 자료 삭제
-- delete from 테이블명 where 조건 <-- 전체 또는 부분적 레코드 삭제 가능
-- truncate table 테이블명 <-- where 조건을 사용x, 전체 레코드 삭제 가능!
DELETE FROM dept WHERE NAME='자재과';
TRUNCATE TABLE dept;

SELECT * FROM dept;

DROP TABLE dept; -- table 자체(구조, 자료)를 삭제시킴

-- 무결성 제약조건 
-- 테이블 생성 시 잘못된 자료 입력을 막고자 다양한 입력 제한 조건을 줄 수 있다
-- 1) 기본키 제약 : primary key(pk) 사용, 중복 레코드 입력 방지가 목적
CREATE TABLE aa(bun INT PRIMARY KEY, irum CHAR(10)); -- bun : not null & unique
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_NAME='aa'
INSERT INTO aa VALUES(1,'tom');
INSERT INTO aa VALUES(2,'tom');
INSERT INTO aa VALUES(2,'james'); -- err발생 이유: pk-2가 있는데 또 2를 입력하려고 해서
INSERT INTO aa(irum) VALUES('tom'); -- err발생 이유 : bun이 없어서
INSERT INTO aa(bun) VALUES(3);

SELECT * FROM aa;

DROP TABLE aa;
-- 1) 같은 표현법 
CREATE TABLE aa(bun INT, irum CHAR(10), CONSTRAINT aa_bun_pk PRIMARY KEY(bun)); -- bun : not null & unique
INSERT INTO aa VALUES(1,'tom');
SELECT * FROM aa;

DROP TABLE aa;

-- 2) check 제약 : 입력 자료의 특정 칼럼값 조건 검사
CREATE TABLE aa(bun INT, nai INT CHECK(nai >= 20));
INSERT INTO aa VALUES(1,30);
INSERT INTO aa VALUES(2,10); -- err발생 이유 : constraint failed

SELECT * FROM aa;

DROP TABLE aa;
-- 3) unique 제약 : 특정 칼럼값 중복 불허
CREATE TABLE aa(bun INT, irum CHAR(10) NOT NULL UNIQUE);
INSERT INTO aa VALUES(1,'tom');
INSERT INTO aa VALUES(2,'james');
INSERT INTO aa VALUES(3,'tom'); -- err 발생 이유 : 'tom'이 중복됨

SELECT * FROM aa;

DROP TABLE aa;
-- 4) foreign key(fk), 외부키, 참조키 제약. 특정 칼럼이 다른 테이블의 칼럼을 참조
-- fk 대상은 pk다!!!
CREATE TABLE jikwon(bun INT PRIMARY KEY, irum CHAR(10) NOT NULL, buser CHAR(10) NOT NULL);
INSERT INTO jikwon VALUES(1,'한송이','인사과');
INSERT INTO jikwon VALUES(2,'이기자','인사과');
INSERT INTO jikwon VALUES(3,'한송이','판매과');

SELECT * FROM jikwon;

CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10) NOT NULL, birth DATETIME, jikwonbun INT, FOREIGN KEY(jikwonbun) REFERENCES jikwon(bun)); -- bun과 jikwonbun의 TYPE은 같아야 한다!!

INSERT INTO gajok VALUES(10,'한가인','2000-01-14',3);
INSERT INTO gajok VALUES(20,'신대웅','2001-04-22',2);
INSERT INTO gajok VALUES(30,'서지민','2001-05-12',2);
SELECT * FROM gajok;

DELETE FROM jikwon WHERE bun=1;
DELETE FROM jikwon WHERE bun=2; -- err 발생 이유 : foreign key의 값과 같이 묶여있기 때문에
DROP TABLE jikwon; -- err 발생 이유 : gajok table에 참조 자료가 있으므로 삭제 불가!
DELETE FROM gajok WHERE jikwonbun=2; -- jikwonbun=2(참조키가 2번)를 지우면 jikwon table의 bun=2를 지울 수 있다.
DELETE FROM jikwon WHERE bun=2; -- -> 참조 가족이 없으므로 2번 직원 삭제 가능!
SELECT * FROM jikwon;

-- 참고
-- CREATE TABLE gajok(CODE INT PRIMARY KEY, ...) on delete cascade  -> 'on delete cascade'라는 옵션을 걸면
-- 직원 자료를 삭제하면 관련있는 가족자료도 함께 지워짐. <-- 위험해서 일반적으로 잘 쓰지 않음.

DROP TABLE jikwon; -- err 발생 : 참조 가족이 아직 남아있으므로.
DELETE FROM gajok WHERE jikwonbun=3;
DROP TABLE gajok;
DROP TABLE jikwon;

-- default : 특정 칼럼에 초기치 부여. null 예방
CREATE TABLE aa(bun INT PRIMARY KEY AUTO_INCREMENT, juso CHAR(20) DEFAULT '강남구 역삼동'); -- auto_increment로 인해 bun이 자동증가함.
INSERT INTO aa VALUES(1, '서초구 서초2동');
INSERT INTO aa(juso) VALUES('서초구 서초3동');
INSERT INTO aa(juso) VALUES('서초구 서초5동');
INSERT INTO aa(bun) VALUES(5);
INSERT INTO aa(bun) VALUES(6);

SELECT * FROM aa;

DROP TABLE aa;


-- index(색인) : 검색 속도 향상을 위해 특정 column에 색인 부여 가능(메모리 많이 잡아먹고 데이터를 재정렬해야돼서 신중하게 판단해야 함)
-- pk column은 자동으로 인덱싱됨.(ascending sort : 오름차순 정렬)
-- index를 자제해야하는 경우 : 입력, 수정, 삭제 등의 작업이 빈번한 경우
CREATE TABLE aa(bun INT PRIMARY KEY, irum VARCHAR(10) NOT NULL, juso VARCHAR(50));
INSERT INTO aa VALUES(1,'신대웅','어린이대공원 화장실 1사로')
ALTER TABLE aa ADD INDEX ind_juso(juso); -- juso columm에 인덱스 부여
SELECT * FROM aa;
EXPLAIN SELECT * FROM aa;
DESCRIBE aa;
SHOW INDEX from aa;
ALTER TABLE aa DROP INDEX ind_juso; -- juso columm에서 인덱스 제거
DROP TABLE aa;
-- 테이블 관련 주요 명령
-- create table (테이블명) ... 만들기
-- alter table (테이블명) ... 바꾸기
-- drop table (테이블명) ... 지우기
CREATE TABLE aa(bun INT, irum VARCHAR(10), juso VARCHAR(50)); 

INSERT INTO aa VALUES(1, '신대웅', '어린이대공원 비상계단');
SELECT * FROM aa;

ALTER TABLE aa RENAME abc; -- 테이블명 변경
SELECT * FROM aa;
ALTER TABLE abc RENAME aa;

-- column 관련 명령
ALTER TABLE aa ADD (job_id INT DEFAULT 10); -- column 추가
SELECT * FROM aa;
ALTER TABLE aa CHANGE job_id job_num INT; -- column 수정
SELECT * FROM aa;
ALTER TABLE aa CHANGE job_num job CHAR(10) DEFAULT '개백수'; -- column 수정
SELECT * FROM aa;
ALTER TABLE aa MODIFY job VARCHAR(10);
SELECT * FROM aa;
DESC aa;
ALTER TABLE aa DROP COLUMN job; -- column 삭제
SELECT * FROM aa;
-- -------------------------------------------------------------------------------------------------------------------------
create table sangdata(code int primary key,sang varchar(20),su int,dan INT);

insert into sangdata values(1,'장갑',3,10000);
insert into sangdata values(2,'벙어리장갑',2,12000);
insert into sangdata values(3,'가죽장갑',10,50000);
insert into sangdata values(4,'가죽점퍼',5,650000);

SELECT * FROM sangdata;
DESC sangdata;

create table buser(
buserno int primary key, 
busername varchar(10) not null,
buserloc varchar(10),
busertel varchar(15));

insert into buser values(10,'총무부','서울','02-100-1111');
insert into buser values(20,'영업부','서울','02-100-2222');
insert into buser values(30,'전산부','서울','02-100-3333');
insert into buser values(40,'관리부','인천','032-200-4444');

SELECT * FROM buser;
DESC buser;

create table jikwon(
jikwonno int primary key,
jikwonname varchar(10) not null,
busernum int not null,
jikwonjik varchar(10) default '사원', 
jikwonpay int,
jikwonibsail date,
jikwongen varchar(4),
jikwonrating char(3),
CONSTRAINT ck_jikwongen check(jikwongen='남' or jikwongen='여'));

insert into jikwon values(1,'홍길동',10,'이사',9900,'2008-09-01','남','a');
insert into jikwon values(2,'한송이',20,'부장',8800,'2010-01-03','여','b');
insert into jikwon values(3,'이순신',20,'과장',7900,'2010-03-03','남','b');
insert into jikwon values(4,'이미라',30,'대리',4500,'2014-01-04','여','b');
insert into jikwon values(5,'이순라',20,'사원',3000,'2017-08-05','여','b');
insert into jikwon values(6,'김이화',20,'사원',2950,'2019-08-05','여','c');
insert into jikwon values(7,'김부만',40,'부장',8600,'2009-01-05','남','a');
insert into jikwon values(8,'김기만',20,'과장',7800,'2011-01-03','남','a');
insert into jikwon values(9,'채송화',30,'대리',5000,'2013-03-02','여','a');
insert into jikwon values(10,'박치기',10,'사원',3700,'2016-11-02','남','a');
insert into jikwon values(11,'김부해',30,'사원',3900,'2016-03-06','남','a');
insert into jikwon values(12,'박별나',40,'과장',7200,'2011-03-05','여','b');
insert into jikwon values(13,'박명화',10,'대리',4900,'2013-05-11','남','a');
insert into jikwon values(14,'박궁화',40,'사원',3400,'2016-01-15','여','b');
insert into jikwon values(15,'채미리',20,'사원',4000,'2016-11-03','여','a');
insert into jikwon values(16,'이유가',20,'사원',3000,'2016-02-01','여','c');
insert into jikwon values(17,'한국인',10,'부장',8000,'2006-01-13','남','c');
insert into jikwon values(18,'이순기',30,'과장',7800,'2011-11-03','남','a');
insert into jikwon values(19,'이유라',30,'대리',5500,'2014-03-04','여','a');
insert into jikwon values(20,'김유라',20,'사원',2900,'2019-12-05','여','b');
insert into jikwon values(21,'장비',20,'사원',2950,'2019-08-05','남','b');
insert into jikwon values(22,'김기욱',40,'대리',5850,'2013-02-05','남','a');
insert into jikwon values(23,'김기만',30,'과장',6600,'2015-01-09','남','a');
insert into jikwon values(24,'유비',20,'대리',4500,'2014-03-02','남','b');
insert into jikwon values(25,'박혁기',10,'사원',3800,'2016-11-02','남','a');
insert into jikwon values(26,'김나라',10,'사원',3500,'2016-06-06','남','b');
insert into jikwon values(27,'박하나',20,'과장',5900,'2012-06-05','여','c');
insert into jikwon values(28,'박명화',20,'대리',5200,'2013-06-01','여','a');
insert into jikwon values(29,'박가희',10,'사원',4100,'2016-08-05','여','a');
insert into jikwon values(30,'최미숙',30,'사원',4000,'2015-08-03','여','b');

SELECT * FROM jikwon;
DESC jikwon;

create table gogek(gogekno int primary KEY, gogekname varchar(10) not NULL, gogektel varchar(20), gogekjumin char(14),
gogekdamsano INT, CONSTRAINT FK_gogekdamsano foreign key(gogekdamsano) references jikwon(jikwonno));

insert into gogek values(1,'이나라','02-535-2580','850612-1156777',5);
insert into gogek values(2,'김혜순','02-375-6946','700101-1054777',3);
insert into gogek values(3,'최부자','02-692-8926','890305-1065777',3);
insert into gogek values(4,'김해자','032-393-6277','770412-2028777',13);
insert into gogek values(5,'차일호','02-294-2946','790509-1062777',2);
insert into gogek values(6,'박상운','032-631-1204','790623-1023777',6);
insert into gogek values(7,'이분','02-546-2372','880323-2558777',2);
insert into gogek values(8,'신영래','031-948-0283','790908-1063777',5);
insert into gogek values(9,'장도리','02-496-1204','870206-2063777',4);
insert into gogek values(10,'강나루','032-341-2867','780301-1070777',12);
insert into gogek values(11,'이영희','02-195-1764','810103-2070777',3);
insert into gogek values(12,'이소리','02-296-1066','810609-2046777',9);
insert into gogek values(13,'배용중','02-691-7692','820920-1052777',1);
insert into gogek values(14,'김현주','031-167-1884','800128-2062777',11);
insert into gogek values(15,'송운하','02-887-9344','830301-2013777',2);

SELECT * FROM gogek;
DESC gogek;
-- ------------------------------------------------------------2.12------------------------------------------------------------------------
-- select : db서버로부터 클라이언트로 자료를 읽는 명령어
-- select 칼럼명 as 별명, ... from 테이블명 where 조건 order by 기준키, ...
SELECT * FROM jikwon; -- mariadb에서 내 로컬로 데이터 가져와서 보여주는거까지
SELECT jikwonno, jikwonname FROM jikwon;
SELECT jikwonno, jikwongen, busernum, jikwonname FROM jikwon; -- 순서는 내 맘대로 설정가능, 이 순서대로 python이 인식함
SELECT jikwonno AS 직원번호, jikwonname AS 직원명 FROM jikwon; -- 별명 설정가능
SELECT 10, '안녕', 12 / 3 AS '4' FROM DUAL; -- 이런 식으로 가상의 테이블을 만들 수 있음
SELECT jikwonname, jikwonpay, jikwonpay * 0.05 AS tax, jikwonpay - jikwonpay * 0.05 AS 실수령 FROM jikwon;
SELECT jikwonname, CONCAT(jikwonname, '님') AS jikwonetc FROM jikwon; -- jikwonname + '님' 가능

-- sort(정렬) : 
SELECT * FROM jikwon ORDER BY jikwonpay ASC; -- order by : 그룹화시킴, asc : 오름차순 정렬
SELECT * FROM jikwon ORDER BY jikwonpay; -- asc은 생략가능, desc는 생략불가, (describe랑 헷갈리지 않게 유의!)
SELECT * FROM jikwon ORDER BY jikwonpay desc; -- desc : 내림차순 정렬
SELECT * FROM jikwon ORDER BY jikwonjik ASC; -- asc : 사전 순으로 오름차순(ㄱ부터)
SELECT * FROM jikwon ORDER BY jikwonjik ASC, busernum DESC, jikwongen ASC, jikwonpay ASC; -- '같은 직급(!!)'에서 번호순 내림차, 번호 같으면 성별로 오름차, 성별 같으면 봉급으로 오름차
SELECT jikwonname, jikwonpay, jikwonpay / 1000 * 1000 AS pay FROM jikwon ORDER BY pay DESC;

SELECT DISTINCT jikwonjik FROM jikwon; -- 중복 배제
SELECT DISTINCT jikwonname FROM jikwon; -- 중복 배제할때는 1개의 column으로만 해야 의미가 있음

-- 연산자 : 괄호() > 산술(*, / > +, -) > 관계(비교) > is null, like, in > between, not > and > or
SELECT * FROM jikwon WHERE jikwonjik = '대리'; -- where조건으로 직급이 대리인 사람만 뽑아옴
SELECT * FROM jikwon WHERE jikwonno = 3;
SELECT * FROM jikwon WHERE jikwonibsail = '2010-03-03';
SELECT * FROM jikwon WHERE jikwonno = 5 OR jikwonno = 7;
SELECT * FROM jikwon WHERE jikwonjik = '사원' AND jikwongen = '여';
SELECT * FROM jikwon WHERE jikwonjik = '사원' AND jikwongen = '여' AND jikwonpay <= 3000;
SELECT * FROM jikwon WHERE jikwonjik = '사원' AND (jikwongen = '여' OR jikwonibsail >= '2017-01-01');

SELECT * FROM jikwon WHERE jikwonno >= 5 AND jikwonno <= 10;
SELECT * FROM jikwon WHERE jikwonno BETWEEN 5 AND 10; -- between은 끝값도 포함하는듯
SELECT * FROM jikwon WHERE jikwonibsail BETWEEN '2017-01-01' AND '2019-12-31';

SELECT * FROM jikwon WHERE jikwonno < 5 or jikwonno > 20;
SELECT * FROM jikwon WHERE jikwonno not BETWEEN 5 AND 20; -- 긍정적 형태의 조건이 속도

SELECT * FROM jikwon WHERE jikwonpay > 5000;
SELECT * FROM jikwon WHERE jikwonpay > 3000 + 2000; -- 산술연산자가 관계연산자보다 우선순위 높아서 윗 코드랑 같은 의미임

SELECT * FROM jikwon WHERE jikwonname = '홍길동';
SELECT * FROM jikwon WHERE jikwonname > '박'; -- 사전상에서 '박'이후의 이름만 나옴
SELECT ASCII('a'), ASCII('A'), ASCII('가'), ASCII('홍길동') FROM DUAL; -- ascii code로 문자의 대소비교가 가능함
SELECT * FROM jikwon WHERE jikwonname BETWEEN '김' AND '홍';

-- in 멤버 조건 연산
SELECT * FROM jikwon WHERE jikwonjik = '대리' OR jikwonjik = '과장' OR jikwonjik = '부장';
SELECT * FROM jikwon WHERE jikwonjik IN('대리', '과장', '부장');
SELECT * FROM jikwon WHERE jikwonno IN(1, 12, 23);

-- like 조건 연산 : %(0개 이상의 문자열), _(한개 문자)
SELECT * FROM jikwon WHERE jikwonname LIKE '이%'; -- 직원명이 '이'로 시작하는 사람 찾기. 첫글자는 '이'여야하고, 두번째부터는 아무 글자가 와도 상관없음
SELECT * FROM jikwon WHERE jikwonname LIKE '이순%'; -- '이순'으로 시작하는 사람 찾기.
SELECT * FROM jikwon WHERE jikwonname LIKE '%라'; -- jikwonname의 column에서 '라'로 끝나는 사람 찾기.
SELECT * FROM jikwon WHERE jikwonname LIKE '이%라'; -- '이'로 시작해서 '라'로 끝나는 사람 찾기.

SELECT * FROM jikwon WHERE jikwonname LIKE '이__'; -- 범위에 제한이 걸려있음. _가 2개이므로, 이로 시작하고 이름이 3글자여야함.
SELECT * FROM jikwon WHERE jikwonname LIKE '이_라'; 
SELECT * FROM jikwon WHERE jikwonname LIKE '__'; -- 이름이 2글자인 사람 찾기

SELECT * FROM jikwon WHERE jikwonpay LIKE '3___'; -- <여기 _3개임
SELECT * FROM jikwon WHERE jikwonpay LIKE '3%';

SELECT * FROM gogek WHERE gogekjumin LIKE '_______1%';
SELECT * FROM gogek WHERE gogekjumin LIKE '%-1%';

SELECT * FROM jikwon;
UPDATE jikwon SET jikwonjik = NULL WHERE jikwonno=5;
SELECT * FROM jikwon;
SELECT * FROM jikwon WHERE jikwonjik = NULL; -- error발생.
SELECT * FROM jikwon WHERE jikwonjik IS NULL; -- is null 활용법

SELECT * FROM jikwon LIMIT 3;
SELECT * FROM jikwon ORDER BY jikwonno DESC LIMIT 3;
SELECT * FROM jikwon LIMIT 5,3; -- 6부터 3개(시작행, 갯수)

SELECT jikwonno AS 직원번호, jikwonname AS 직원명, jikwonjik AS 직급, jikwonpay AS 연봉, jikwonpay/12 보나스, jikwonibsail AS 입사일 FROM jikwon
WHERE jikwonjik IN('과장', '부장', '사원') AND jikwonpay>= 4000 AND jikwonibsail BETWEEN '2015-01-01' AND '2019-12-31' ORDER BY jikwonjik, jikwonpay DESC LIMIT 3;

-- 내장함수 : 데이터 조작의 효율성 증진이 목적
-- 단일 행 함수 : 각 행에 대해 작업한다. 핸 단위 처ㅣㄹ
-- 문자 함수
SELECT LOWER('Hello'), UPPER('Hello') FROM DUAL;
SELECT SUBSTR('hello world', 3), SUBSTR('hello world', 3, 3), SUBSTR('hello world', -3, 3) FROM DUAL;
SELECT length('hello world'), inSTR('hello world', 'e') FROM DUAL;
SELECT REPLACE('010-1111-1234', '.','-') FROM DUAL;

-- ...
-- jikwon 테이블에서 이름에 '이'가 포함된 직원이 있으면 '이'부터 두글자 출력하기
select jikwonname, SUBSTR(jikwonname, INSTR(jikwonname, '이'), 2) FROM jikwon WHERE jikwonname LIKE '%이%';

-- 숫자 함수
SELECT ROUND(45.678, 2), ROUND(45.678), ROUND(45.678, 0), ROUND(45.678, -1) FROM DUAL;
SELECT jikwonname, jikwonpay, jikwonpay * 0.25 AS tax, ROUND(jikwonpay * 0.25, 0) FROM jikwon;

SELECT TRUNCATE(45.678, 0), TRUNCATE(45.678, 1), TRUNCATE(45.678, -1) FROM DUAL; -- 뒷자리는 버리기, 내림이라고 생각하면 될듯?
SELECT MOD(15, 2), 15 / 2 FROM DUAL; -- 나머지
SELECT GREATEST(23,25,1,12,100), LEAST(23,25,1,12,100) FROM DUAL;

-- 날짜 함수
SELECT NOW(), NOW() + 2, SYSDATE(), CURDATE() FROM DUAL;
SELECT NOW(), SLEEP(3), NOW() FROM DUAL; -- 하나의 query 내에서는 동일 값 출력
SELECT SYSDATE(), SLEEP(3), SYSDATE() FROM DUAL; -- 실행 시점값 출력
SELECT ADDDATE('2020-08-01', 3), ADDDATE('2020-08-01', -3), SUBDATE('2020-08-01', 3) FROM DUAL; -- 날짜 더하고 빼기(윤년도 체크함)

SELECT DATE_ADD(NOW(), INTERVAL 1 MINUTE), DATE_ADD(NOW(), INTERVAL 5 DAY), DATE_ADD(NOW(), INTERVAL 5 MONTH) FROM DUAL;

SELECT DATEDIFF(NOW(), '2025-05-05') FROM DUAL;

-- 형변환 함수
SELECT NOW(), DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(), '%Y년%m월%d일')
SELECT jikwonname, jikwonibsail, DATE_FORMAT(jikwonibsail, '%w') FROM jikwon WHERE busernum=10;

SELECT STR_TO_DATE('2026-02-12', '%Y-%m-%d');
SELECT STR_TO_DATE('2026-02-12 13:16:34', '%Y-%m-%d %H:%i:%S');

-- 기타 함수
-- rank() : 순위 결정
SELECT jikwonno, jikwonname, jikwonpay, RANK() OVER (ORDER BY jikwonpay desc) AS result, dense_RANK() OVER (ORDER BY jikwonpay desc) AS result2 FROM jikwon;
-- (아무것도 안쓰면 asc, desc쓰면 내림차순)(예시 : order by jikwonpay desc)

-- nvl(value1, value2) : value1이 null이면 value2를 취함.
SELECT jikwonname, jikwonjik, nvl(jikwonjik, '임시직') FROM jikwon;

-- nvl2(value1, value2, value3) : value1이 null이 아니면 value2, null이면 value3으로 출력함
SELECT jikwonname, jikwonjik, nvl2(jikwonjik, '정규직', '임시직') FROM jikwon;

-- nullif(value1, value2) : 2개의 값이 일치하면 null, 아니면 value1 취함
SELECT jikwonname, jikwonjik, NULLIF(jikwonjik, '대리') FROM jikwon;

-- 조건 표현식
-- 형식 1)
-- case 표현식 when 비교값1 then 결과값1 when 비교값2 then 결과값2 ... [else 결과값n] end as 별명
SELECT case 10 / 2 when 5 then '안녕' when 2 then '반가워'  ELSE '잘가' END AS result FROM DUAL;

SELECT jikwonname, jikwonpay, jikwonjik, 
case jikwonjik 
when '이사' then jikwonpay*0.05 
when '부장' then jikwonpay*0.04 
when '과장' then jikwonpay*0.03 
ELSE jikwonpay*0.02 END as donation FROM jikwon;

-- 형식 2)
-- case when 조건1 then 결과값1 when 조건2 then 결과값2 ... [else 결과값n] end as 별명
SELECT jikwonname, case 
when jikwongen='남' then '눈치' 
when jikwongen='여' then '안볼래' 
END AS gender FROM jikwon;

SELECT jikwonname, jikwonpay, case 
when jikwonpay >= 7000 then '향정신성약물이내몸에퍼졌어' 
when jikwonpay >= 5000 then '도익환은댄스머신'
ELSE '야관문고투더문' END AS result, jikwongen FROM jikwon WHERE jikwonjik IN('대리', '과장');

-- if(조건, 참값, 거짓값) as 별명
SELECT jikwonname, jikwonpay, jikwonjik, if(TRUNCATE(jikwonpay/1000, 0) >= 5, 'good', 'normal') AS result FROM jikwon; 

-- 복수행 함수(집계함수) : 전체 자료를 그룹별로 구분해 통계 결과를 얻기 위한 함수
SELECT sum(jikwonpay) AS 합, AVG(jikwonpay) AS 평균 FROM jikwon;
SELECT max(jikwonpay) AS 최대, min(jikwonpay) AS 최소 FROM jikwon;

SELECT * FROM jikwon;
UPDATE jikwon SET jikwonpay=NULL WHERE jikwonno=5;
DESC jikwon;

SELECT AVG(jikwonpay), AVG(nvl(jikwonpay,0)) FROM jikwon; -- 집계함수는 null을 작업하지 않는다(null은 작업에서 제외됨)
SELECT sum(jikwonpay) / 29, SUM(nvl(jikwonpay,0)) / 30 FROM jikwon; -- null을 작업하고싶으면 nvl로 0이라는 value를 줘야한다.

SELECT COUNT(jikwonno), COUNT(jikwonpay), COUNT(jikwonjik) FROM jikwon;
SELECT stddev(jikwonpay) AS 표준편차, VAR_SAMP(jikwonpay) as 분산 FROM jikwon;
SELECT COUNT(*) AS 인원수 FROM jikwon; -- >가장 일반적으로 갯수를 세는 경우임.

SELECT COUNT(*) AS 인원, stddev(jikwonpay) AS 표준편차, VAR_SAMP(jikwonpay) as 분산 FROM jikwon WHERE busernum=10;
SELECT COUNT(*) AS 인원, stddev(jikwonpay) AS 표준편차, VAR_SAMP(jikwonpay) as 분산 FROM jikwon WHERE busernum=20;

-- 과장이 몇명인지? 
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonjik='과장';

-- 2010년 이전에 입사한 남직원은 몇명?
SELECT COUNT(*) AS '2010년 이전에 입사한 남직원' FROM jikwon WHERE jikwonibsail < '2010-1-1' AND jikwongen='남';

-- 2015년 이후에 입사한 여직원의 연봉합, 평균, 인원수는?
SELECT SUM(jikwonpay) AS 연봉합, AVG(jikwonpay) AS 연봉평균, COUNT(*) AS 인원수 FROM jikwon WHERE jikwonibsail > '2015-1-1' AND jikwongen='여';
-- ---------------------------------------------------2.13-------------------------------------------------
-- 그룹함수 : group by 절 : 소계출력
-- select 그룹칼럼명, 계산함수, ... from 테이블명 where 조건 group by 그룹칼럼명 having 조건
-- 그룹칼럼에 대해 order by 할 수 없음. 단 출력 결과는 order by 가능

-- 성별 연봉 평균, 인원수를 출력하기
SELECT jikwongen, AVG(jikwonpay), COUNT(*) FROM jikwon GROUP BY jikwongen;

-- 부서별 연봉합
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum;

-- 부서별 연봉합 : 연봉합이 35000이상인 경우만 출력
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum HAVING SUM(jikwonpay) >= 35000;

-- 부서별 연봉합 : 여성만, 숫자도 출력하기
SELECT busernum, SUM(jikwonpay), COUNT(*) FROM jikwon where jikwongen= '여' GROUP BY busernum;

-- 부서별 연봉합 : 연봉합이 15000 이상인 여성만!
SELECT busernum, SUM(jikwonpay), COUNT(*) FROM jikwon where jikwongen= '여' GROUP BY busernum HAVING SUM(jikwonpay) >= 15000;

SELECT busernum, SUM(jikwonpay) AS paytotal, COUNT(*) FROM jikwon where jikwongen= '여' GROUP BY busernum HAVING paytotal >= 15000;

-- 주의
SELECT busernum, SUM(jikwonpay) FROM jikwon order by busernum GROUP BY busernum; -- < group by 전에 order by는 syntax error발생!
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum order by SUM(jikwonpay) DESC; -- group by 뒤에 order by는 가능!

-- join !! : 하나 이상의 테이블에서 원하는 자료 추출
-- 반드시 공통 칼럼이 필요하다

DESC buser;
DESC jikwon;
DESC gogek;

INSERT INTO buser(buserno, busername) VALUES(50,'기획실');

SELECT * FROM jikwon;
ALTER TABLE jikwon MODIFY busernum INT NULL;
UPDATE jikwon SET busernum=NULL WHERE jikwonno=5
SELECT * FROM jikwon;

SELECT test.jikwon.jikwonname FROM jikwon;
SELECT mytab.jikwonname FROM jikwon AS mytab;

-- cross join : 한 쪽 테이블의 모든 행과 다른 쪽 테이블의 모든 행을 join하는 기능
SELECT jikwonname, busername FROM jikwon, buser;
SELECT jikwonname, busername FROM jikwon CROSS join buser; -- 이게 표준 SQL
SELECT * FROM buser;

-- cross join 중 self join
SELECT a.jikwonname, b.jikwonname FROM jikwon a, jikwon b;

-- EQUI join : 조인 조건식에 '='사용. 두 테이블은 '같다' 조건으로 join
-- 대부분의 pk-fk join은 EQUI join이다.
SELECT jikwonname, busername FROM jikwon, buser WHERE jikwon.busernum = buser.buserno; -- >null은 빼고 함

-- non-EQUI join : 조인 조건식에 '=' 이외의 관계연산자를 사용
CREATE TABLE paygrade(grade INT PRIMARY KEY, lpay INT, hpay INT);
INSERT INTO paygrade VALUES(1,0,1999);
INSERT INTO paygrade VALUES(2,2000,2999);
INSERT INTO paygrade VALUES(3,3000,3999);
INSERT INTO paygrade VALUES(4,4000,4999);
INSERT INTO paygrade VALUES(5,5000,9999);
SELECT * FROM paygrade;

SELECT jiktab.jikwonname, jiktab.jikwonpay, paytab.grade FROM jikwon AS jiktab, paygrade AS paytab
WHERE jiktab.jikwonpay >= paytab.lpay AND jiktab.jikwonpay <= paytab.hpay;

-- inner join : 두 테이블을 조인할 때, 두 테이블에 모두 지정한 열의 데이터가 있는 경우만 추출
SELECT jikwonno, jikwonname, busername FROM jikwon, buser WHERE jtab.busernum=btab.buserno; -- oracle에서 주로 사용
SELECT jtab.jikwonno, jtab.jikwonname, btab.busername FROM jikwon AS jtab, buser as btab WHERE jtab.busernum=btab.buserno;

SELECT jikwonno, jikwonname, busername FROM jikwon, buser WHERE busernum=buserno AND jikwongen='남'; -- where 조건에 join 조건 + record 제한 조건 : 가독성 나쁨

-- EQUI join : 
SELECT jikwonno, jikwonname, busername FROM jikwon INNER JOIN buser ON busernum=buserno;

SELECT jikwonno, jikwonname, busername FROM jikwon INNER JOIN buser ON busernum=buserno WHERE jikwongen='남';

-- outer join : 두 테이블을 조인할 때 1개의 테이블에만 자료가 있어도 결과 추출
-- left outer join(oracle용)
SELECT jikwonno, jikwonname, busername FROM jikwon, buser WHERE busernum=buserno(+); -- oracle용

-- right outer join(oracle용)
SELECT jikwonno, jikwonname, busername FROM jikwon, buser WHERE busernum(+)=buserno; -- oracle용

-- left outer join
SELECT jikwonno, jikwonname, busername FROM jikwon LEFT OUTER JOIN buser ON busernum=buserno; -- null도 출력함. 직원이 왼쪽에 있으므로 직원이 다 나옴.

-- right outer join
SELECT jikwonno, jikwonname, busername FROM jikwon RIGHT OUTER JOIN buser ON busernum=buserno; -- 오른쪽인 buser의 값이 다 나온다.

-- full outer join(oracle용)
SELECT jikwonno, jikwonname, busername FROM jikwon FULL OUTER JOIN buser ON busernum=buserno; -- oracle용

SELECT jikwonno, jikwonname, busername FROM jikwon LEFT OUTER JOIN buser ON busernum=buserno
UNION 
SELECT jikwonno, jikwonname, busername FROM jikwon RIGHT OUTER JOIN buser ON busernum=buserno; -- mariadb용(left, right를 진행하고 union으로 합침)

SELECT jikwonno AS 직원번호, jikwonname AS 직원명, busername AS 부서명 FROM jikwon INNER JOIN buser ON busernum=buserno WHERE jikwongen='남' AND jikwonname LIKE '김%';

SELECT SUM(jikwonpay) AS hap, COUNT(*) AS COUNT FROM jikwon INNER JOIN buser ON busernum=buserno WHERE jikwongen='남';

SELECT * FROM gogek; -- buser table과는 join불가하다.(공통 column이 없음, jikwon&buser + buser&gogek은 가능!)

-- 세 개의 테이블 join : 두 개를 먼저 join 후 그 결과와 나머지 테이블로 join!
SELECT jikwonname, busername, gogekname FROM jikwon, buser, gogek WHERE busernum=buserno AND jikwonno=gogekdamsano;

SELECT jikwonname, busername, gogekname FROM jikwon 
INNER JOIN buser ON busernum=buserno
INNER JOIN gogek on jikwonno=gogekdamsano;

-- union : 구조가 일치하는 두 개 이상의 테이블 자료 합쳐 출력. 원래의 테이블 계속 유지
CREATE TABLE pum1(bun INT, pummok VARCHAR(20));
INSERT INTO pum1 VALUES(1,'파파야');
INSERT INTO pum1 VALUES(2,'한라봉');
INSERT INTO pum1 VALUES(3,'오렌지');
SELECT * FROM pum1;

CREATE TABLE pum2(mum INT, sangpum VARCHAR(20));
INSERT INTO pum2 VALUES(10,'토마토');
INSERT INTO pum2 VALUES(20,'딸기');
INSERT INTO pum2 VALUES(30,'참외');
INSERT INTO pum2 VALUES(40,'수박');
SELECT * FROM pum2;

SELECT bun AS 번호, pummok AS 품명 FROM pum1
UNION
SELECT mum, sangpum FROM pum2;

-- subquery ☆☆☆ : query 내에 query가 있는 형태(주로 안쪽 질의 결과를 바깥쪽 질의에서 참조)
-- 다른 테이블의 결과를 조건으로 쓰고 싶을 때
-- 계산된 값을 이용하고 싶을 때
-- 복잡한 조건을 단계적으로 나눠 처리하고 싶을 때

-- where 안에 있는 subquery
-- '이미라' 직원과 직급이 같은 직원 출력
SELECT * FROM jikwon;
SELECT * FROM buser;
SELECT * FROM gogek;

SELECT jikwonjik FROM jikwon WHERE jikwonname='이미라';
SELECT * FROM jikwon WHERE jikwonjik='대리';

SELECT * FROM jikwon 
WHERE jikwonjik=(SELECT jikwonjik FROM jikwon WHERE jikwonname='이미라');

-- 직급이 대리 중에서 가장 먼저 입사한 직원은?
SELECT * FROM jikwon 
WHERE jikwonjik='대리' AND 
jikwonibsail=(SELECT MIN(jikwonibsail) FROM jikwon WHERE jikwonjik='대리');

-- 인천에 근무하는 직원 출력
SELECT * FROM jikwon
WHERE busernum = (SELECT buserno FROM buser WHERE buserloc='인천');

-- 인천에서 근무하는 직원 출력
SELECT * FROM jikwon
WHERE busernum in(SELECT buserno FROM buser WHERE NOT buserloc='인천'); -- > 괄호 안의 값이 복수형이므로 in으로 받아내야 오류가 안나옴

SELECT * FROM jikwon WHERE busernum <> (SELECT buserno FROM buser WHERE buserloc='인천'); -- < 인천 이외에 근무하는 직원 출력

-- 고객 중 차일호와 나이가 같은 자료 출력
SELECT * FROM gogek
WHERE SUBSTR(gogekjumin,1,2)=(SELECT SUBSTR(gogekjumin,1,2) FROM gogek WHERE gogekname='차일호'); -- < substr1,2는 gogekjumin의 (1)첫번째에서 (2)만큼으을 출력
-- ------------------------------------------------2.23-------------------------------------------------------------------------------
-- 쿼리문은 동일한 결과를 여러 방법으로 수행 가능
-- 총무부에 근무하는 직원들이 관리하는 고객 출력
-- subquery 사용
SELECT gogekno, gogekname, gogektel FROM gogek 
WHERE gogekdamsano IN(SELECT jikwonno FROM jikwon WHERE busernum=(SELECT buserno FROM buser WHERE busername='총무부'));
-- join 사용
SELECT gogekno, gogekname, gogektel FROM gogek 
INNER JOIN jikwon ON jikwon.jikwonno=gogek.gogekdamsano
INNER JOIN buser ON jikwon.busernum=buser.buserno
WHERE busername='총무부';

-- any, all 연산자 : null인 자료는 제외하고 작업.
-- <any : subquery의 반환값 중 최대값보다 작은 ~
-- >any : subquery의 반환값 중 최소값보다 큰 ~
-- <all : subquery의 반환값 중 최소값보다 작은 ~
-- >all : subquery의 반환값 중 최대값보다 큰~

-- '대리'의 최대값보다 작은 연봉을 받는 직원은??
SELECT * FROM jikwon WHERE jikwonpay < ANY(SELECT jikwonpay FROM jikwon WHERE jikwonjik='대리');

-- 30번 부서의 최고 연봉자보다 연봉을 많이 받는 직원은?
SELECT * FROM jikwon WHERE jikwonpay > ALL(SELECT jikwonpay FROM jikwon WHERE busernum=30);

-- 30번 부서의 최저 연봉자보다 연봉을 많이 받는 직원은?
SELECT * FROM jikwon WHERE jikwonpay > ANY(SELECT jikwonpay FROM jikwon WHERE busernum=30);

-- exists 연산자
-- 직원이 있는 부서 출력
SELECT busername, buserloc FROM buser bu
WHERE EXISTS(SELECT 'imsi' FROM jikwon WHERE jikwon.busernum=bu.buserno); -- true 반환

-- 직원이 없는 부서 출력
SELECT busername, buserloc FROM buser bu
WHERE NOT EXISTS(SELECT 'imsi' FROM jikwon WHERE jikwon.busernum=bu.buserno); -- false 반환

-- from 절에 사용하는 subquery
-- 전체 평균 연봉과 최대 연봉 사이의 연봉을 받는 직원 출력
SELECT jikwonno, jikwonname, jikwonpay 
FROM jikwon a, (SELECT AVG(jikwonpay) avgs, MAX(jikwonpay) maxs FROM jikwon) b
WHERE a.jikwonpay BETWEEN b.avgs AND b.maxs;

-- group by의 having절에 포함된 subquery
-- 부서별 평균 연봉 중 30번 부서의 평균 연봉보다 큰 부서 출력
SELECT busernum, AVG(jikwonpay) FROM jikwon
GROUP BY busernum HAVING AVG(jikwonpay) > (SELECT AVG(jikwonpay) FROM jikwon WHERE busernum=30);

-- 상관 subquery : outer query의 각 행을 inner query에서 참조하여 수행하는 subquery
-- 안쪽 질의에서 바깥쪽 질의를 참조하고, 다시 안쪽의 결과를 바깥쪽 질의에서 참조하는 형태
-- 각 부서의 최대 연봉자는?
SELECT * FROM jikwon a
WHERE a.jikwonpay=(SELECT MAX(b.jikwonpay) FROM jikwon b WHERE a.busernum=b.busernum);

-- 연봉 순위 3위 이내의 직원 출력(descending)
SELECT a.jikwonno, a.jikwonname, a.jikwonpay FROM jikwon a
WHERE 3 > (SELECT COUNT(*) FROM jikwon b WHERE b.jikwonpay > a.jikwonpay)
AND jikwonpay IS NOT NULL;

-- subquery를 이용한 table 생성 및 insert 수행
CREATE TABLE jiktab1 AS SELECT * FROM jikwon; -- jikwon과 동일 테이블 생성. 근데 private key는 제외
DESC jiktab1;
DESC jikwon;
SELECT * FROM jiktab1;

CREATE TABLE jiktab2 AS SELECT * FROM jikwon WHERE 1=0; -- jikwon과 동일 구조 테이블 생성. 
SELECT * FROM jiktab2;
DESC jiktab2;
INSERT INTO jiktab2 SELECT * FROM jikwon WHERE jikwonjik='과장';
SELECT * FROM jiktab2;

INSERT INTO jiktab2(jikwonno, jikwonname, busernum) SELECT jikwonno, jikwonname, busernum FROM jikwon
WHERE jikwonjik='대리'; 
SELECT * FROM jiktab2;

-- update + subquery
SELECT * FROM jiktab1;
UPDATE jiktab1 SET jikwonjik=(SELECT jikwonjik FROM jikwon WHERE jikwonname='이순신') WHERE jikwonno=2;

-- delete + subquery
DELETE FROM jiktab1 WHERE jikwonno IN(SELECT DISTINCT gogekdamsano FROM gogek);
SELECT * FROM jiktab1;

-- 트랜잭션(transaction) : DB의 상태를 변경시키는 논리적 작업 단위, 원래는 자동으로 처리됨. 수동으로 변환시켜서 하는 것
-- 트랜잭션의 4가지 특징: ACID
-- insert, update, delete시 자동으로 트랜잭션 시작
-- commit, rollback으로 트랜잭션 종료
-- 서버종료, timeout 등이 발생해도 트랜잭션 종료
SHOW VARIABLES LIKE 'autocommit%'; -- autocommit 설정 확인
SET autocommit = TRUE -- autocommit 설정
SET autocommit = FALSE -- autocommit 해제

-- 트랜잭션 연습
CREATE TABLE jiktab3 AS SELECT * FROM jikwon; -- 연습용 테이블
SET autocommit = FALSE

-- 연습1
DELETE FROM jiktab3 WHERE jikwonno=2; -- 트랜잭션 시작
SELECT * FROM jiktab3;
ROLLBACK; -- 트랜잭션 종료(jikwonno 2번 지운게 취소됨, DB서버와 관련없이 해당 컴에서만 진행)
COMMIT; -- 트랜잭션 종료(DB서버에 현재 클라이언트의 내용을 근거로 원본 갱신)
SET autocommit = TRUE;


-- 연습2 : savepoint를 이용해 부분적인 트랜잭션 처리 가능
SET autocommit = FALSE;
SELECT * FROM jiktab3;
UPDATE jiktab3 SET jikwonpay=4500 WHERE jikwonno=4; -- 트랜잭션 시작
SAVEPOINT a;
UPDATE jiktab3 SET jikwonpay=8888 WHERE jikwonno=5; 
SELECT * FROM jiktab3;
ROLLBACK TO SAVEPOINT a; -- 부분 작업 취소 : 트랜잭션 종료 X
SELECT * FROM jiktab3;
ROLLBACK; -- 전체 작업 취소 : 트랜잭션 종료!
SELECT * FROM jiktab3;

UPDATE jiktab3 SET jikwonpay=9999 WHERE jikwonno=5; -- 트랜잭션 시작
COMMIT; -- 트랜잭션 종료
SET autocommit = TRUE;
SHOW VARIABLES LIKE 'autocommit%';

-- 교착상태(deadlock) : 두 개 이상의 트랜잭션이 서로 상대방이 가진 락(lock)을 기다리면서 영원히 진행하지 못하는 상태
-- 해결책은 트랜잭션을 수행완료 또는 취소하면 된다.
-- 일관성 유지가 중요
-- 프롬프트, heidiSQL로 2명의 사용자가 같은 테이블을 수정할 때 deadlock 발생 가능함
-- 이때 한쪽에서 commit/rollback으로 트랜잭션을 종료시키면 다른 한쪽도 무한루프에서 빠질 수 있음
SET autocommit = FALSE;
SELECT * FROM jiktab3 WHERE jikwonno=7;
UPDATE jiktab3 SET jikwonpay=1234 WHERE jikwonno=7; -- 트랜잭션 시작
COMMIT; -- 트랜잭션 종료
SET autocommit = TRUE;

-- view 파일 ---------------------------------
-- 물리적인 테이블을 근거로 select문을 파일로 저장하여 가상의 테이블로 사용한다.
-- 물리적인 테이블이 아니므로 메모리 소모가 거의 없다.
-- 복잡하고 긴 쿼리문을 단순화 가능, 보안 강화, 자료의 독립성 확보
-- 형식 : create [or replace] view 뷰파일명 as select문
-- 		 alter view 뷰파일명 ~
-- 		 drop view 뷰파일명 ~

SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';

CREATE OR REPLACE VIEW v_a AS 
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';

SHOW TABLES;
SELECT * FROM v_a;
DESC v_a;

SHOW FULL TABLES IN test WHERE table_type LIKE 'view'; -- view file 목록 확인
SELECT SUM(jikwonpay) AS 연봉합 FROM v_a;

CREATE VIEW v_b AS 
SELECT * FROM jikwon WHERE jikwonname LIKE '김%' OR jikwonname LIKE '이%' OR jikwonname LIKE '박%';

SELECT * FROM v_b;
SELECT jikwonno, jikwonname, jikwonpay FROM v_b WHERE jikwonjik='사원';

ALTER TABLE jikwon RENAME kbs;
SELECT * FROM v_b;

ALTER TABLE kbs RENAME jikwon;
SELECT * FROM v_b;

CREATE VIEW v_c AS SELECT * FROM jikwon ORDER BY jikwonpay DESC;
SELECT * FROM v_c;

CREATE VIEW v_d AS SELECT jikwonno, jikwonname, jikwonpay * 10000 as ypay FROM jikwon;
SELECT * FROM v_d;

CREATE VIEW v_e AS SELECT jikwonname, ypay FROM v_d WHERE ypay >= 50000000;
SELECT * FROM v_e; -- view로 view를 만들 수도 있음!

UPDATE v_e SET jikwonname='김치국' WHERE jikwonname='김부만'; 
SELECT * FROM v_e;
SELECT * FROM v_d;
SELECT * FROM jikwon; -- > view파일을 수정하면 원본 테이블을 수정하는 것과 같음.

DELETE FROM v_d WHERE jikwonname='최미숙';
SELECT * FROM jikwon; -- > view파일을 수정하면 원본 테이블을 수정하는 것과 같음.

DELETE FROM v_d WHERE ypay=41000000; -- 계산에 의한 열도 조건에 참여 가능
SELECT * FROM v_d;
SELECT * FROM jikwon;

SELECT * FROM v_d;
UPDATE v_d SET ypay=1111 WHERE jikwonname='홍길동'; -- error 발생. view파일의 계산 column은 수정 불가능함

CREATE OR REPLACE view v_e AS SELECT jikwonno, jikwonname, busernum, jikwonpay FROM jikwon;
SELECT * FROM v_e;
INSERT INTO v_e VALUES(31,'감스트', 20, 5000); -- < view파일로 insert가능, view의 insert는 원본 not null에 주의
SELECT * FROM jikwon;

DESCRIBE jikwon;

CREATE OR REPLACE view v_f AS 
SELECT jikwonno, jikwonname, busernum, jikwonpay, jikwonibsail FROM jikwon WHERE jikwonibsail < '2015-1-1';
SELECT * FROM v_f;

INSERT INTO v_f VALUES(32, '철구', 10, 6000,'2014-5-6');
INSERT INTO v_f VALUES(33, '커맨더지코', 10, 7000,'2025-5-6'); -- < v_f는 jikwonibsail이 2015-1-1이전의 사람만 나타내서 insert는 됐는데 표시되지 않음
SELECT * FROM v_f;
SELECT * FROM jikwon;

CREATE VIEW v_group AS SELECT jikwonjik, SUM(jikwonpay) AS 합, AVG(jikwonpay) AS 평균 FROM jikwon GROUP BY jikwonjik;
SELECT * FROM v_group; -- group by에 의한 view는 참조만 가능(insert, update, delete X)

CREATE OR REPLACE VIEW v_join AS SELECT jikwonno, jikwonname, busername, jikwonjik FROM jikwon 
INNER JOIN buser ON jikwon.busernum=buser.buserno
WHERE jikwon.busernum IN(10,20);

SELECT * FROM v_join;

UPDATE v_join SET jikwonname='손오공' WHERE jikwonname='박명화';
SELECT * FROM v_join;

UPDATE v_join SET jikwonname='사오정', busername='영업부' WHERE jikwonname='손오공';
-- join에 의한 view는 한 개의 테이블만 수정에 참여해야 함.

DELETE FROM v_join WHERE jikwonname='손오공'; -- < join에 의한 삭제 불가능!