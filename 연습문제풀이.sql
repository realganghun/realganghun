문1) 직급별 급여의 평균 (NULL인 직급 제외) *
SELECT nvl(jikwonjik,'임시직'), nvl(AVG(jikwonpay),0) FROM jikwon GROUP BY jikwonjik ORDER BY AVG(jikwonpay);
문2) 부장,과장에 대해 직급별 급여의 총합*
SELECT jikwonjik AS 직급, SUM(jikwonpay) AS '급여의 총합' FROM jikwon where jikwonjik = '부장'or jikwonjik = '과장' GROUP BY jikwonjik;
문3) 2015년 이전에 입사한 자료 중 년도별 직원수 출력 *
SELECT date_format(jikwonibsail, '%Y') AS 입사년도, COUNT(*) AS '년도별 직원수' FROM jikwon where jikwonibsail <= '2015-01-01' GROUP BY date_format(jikwonibsail, '%Y');
문4) 직급별 성별 인원수, 급여합 출력 (NULL인 직급은 임시직으로 표현) *
SELECT nvl(jikwonjik, '임시직') AS 직급, COUNT(jikwongen) AS '성별 인원수', nvl(SUM(jikwonpay),0) as 급여합 FROM jikwon GROUP BY jikwonjik;
SELECT nvl(jikwonjik, '임시직') AS 직급, jikwongen as 성별, COUNT(*) AS 인원수, nvl(SUM(jikwonpay),0) as 급여합 FROM jikwon GROUP BY jikwonjik, jikwongen;
문5) 부서번호 10,20에 대한 부서별 급여 합 출력*
SELECT busernum AS 부서번호, SUM(jikwonpay) AS 급여합 FROM jikwon WHERE busernum = 10 OR busernum = 20 GROUP BY busernum;
SELECT busernum AS 부서번호, SUM(jikwonpay) AS 급여합 FROM jikwon WHERE busernum IN(10, 20) GROUP BY busernum;
문6) 급여의 총합이 7000 이상인 직급 출력(NULL인 직급은 임시직으로 표현) *
SELECT nvl(jikwonjik, '임시직') AS 직급, avg(jikwonpay) as 평균임금 FROM jikwon GROUP BY jikwonjik HAVING avg(jikwonpay) >= 7000;
문7) 직급별 인원수, 급여합계를 구하되 인원수가 3명 이상인 직급만 출력(NULL인 직급은 임시직으로 표현) *
SELECT nvl(jikwonjik,'임시직') AS 직급, COUNT(*) AS 인원수, nvl(SUM(jikwonpay),0) AS 급여합계 FROM jikwon GROUP BY jikwonjik HAVING COUNT(*) >= 3;



JOIN 연습1 ---------------

문1) 직급이 '사원' 인 직원이 관리하는 고객자료 출력
출력 ==>  사번   직원명   직급      고객명    고객전화    고객성별
                   3     한국인   사원       우주인    123-4567       남

SELECT * FROM jikwon;
SELECT * FROM gogek;

SELECT jikwonno AS 사번, jikwonname AS 직원명, jikwonjik AS 직급, gogekname AS 고객명, gogektel AS 고객전화, case
when gogekjumin LIKE '%-1%' then '남'
when gogekjumin LIKE '%-2%' then '여' END AS 고객성별 
FROM jikwon, gogek WHERE jikwonjik = '사원' AND jikwonno=gogekdamsano;

SELECT jikwonno AS 사번, jikwonname AS 직원명, jikwonjik AS 직급, gogekname AS 고객명, gogektel AS 고객전화, case
when SUBSTR(gogekjumin, 8, 1) IN('1','3') then '남'
when SUBSTR(gogekjumin, 8, 1) IN('2','4') then '여' END AS 고객성별
FROM jikwon INNER JOIN gogek on jikwonno=gogekdamsano WHERE jikwonjik = '사원';
문2) 직원별 고객 확보 수  -- GROUP BY 사용
    - 모든 직원 참여

SELECT jikwonname AS 직원이름, nvl(jikwonjik,'임시직') AS 직급, COUNT(*) AS '고객 확보 수' FROM jikwon, gogek where jikwonno=gogekdamsano GROUP BY jikwonname;

SELECT jikwonname AS 직원이름, nvl(jikwonjik,'임시직') AS 직급, COUNT(gogekname) AS '고객수' FROM jikwon LEFT OUTER JOIN gogek ON jikwonno=gogekdamsano GROUP BY jikwonname;
문3) 고객이 담당직원의 자료를 보고 싶을 때 즉, 고객명을 입력하면,  담당직원 자료 출력  

        :    ~ WHERE GOGEK_NAME='강나루'
출력 ==>  직원명       직급
                한국인       사원

SELECT jikwonname AS 직원명, jikwonjik AS 직급 FROM jikwon,gogek WHERE gogekname='강나루' AND gogekdamsano=jikwonno;

SELECT jikwonname AS 직원명, jikwonjik AS 직급 FROM jikwon inner join gogek on gogekdamsano=jikwonno WHERE gogekname='강나루';
문4) 직원명을 입력하면 관리고객 자료 출력
       : ~ WHERE JIKWON_NAME='이순신'
출력 ==> 고객명   고객전화          주민번호           나이
               강나루   123-4567    700512-1234567      38

SELECT gogekname AS 고객명, gogektel AS 고객전화, gogekjumin AS 주민번호, 126 - (gogekjumin DIV 10000) AS 나이 FROM jikwon, gogek WHERE jikwonname='이순신' AND gogekdamsano=jikwonno;


JOIN 연습2 ---------------
SELECT * FROM jikwon;
SELECT * FROM gogek;
SELECT * FROM buser;
문1) 총무부에서 관리하는 고객수 출력 (고객 30살 이상만 작업에 참여)
SELECT busername AS 부서, COUNT(*) AS 고객수 FROM jikwon, gogek, buser 
WHERE busernum=buserno 
AND jikwonno=gogekdamsano 
AND busername='총무부' 
AND 126 - (gogekjumin DIV 10000) > 30;


문2) 부서명별 고객 인원수 (부서가 없으면 "무소속")
SELECT busername as 부서명, COUNT(*) AS 고객수 FROM jikwon, gogek, buser 
WHERE busernum=buserno 
AND jikwonno=gogekdamsano 
GROUP BY nvl(busernum,'무소속');

SELECT nvl(busername, '무소속') as 부서명, COUNT(gogekno) AS 고객수 FROM jikwon 
LEFT OUTER JOIN buser ON busernum = buserno 
INNER JOIN gogek ON jikwonno=gogekdamsano 
GROUP BY busername;

문3) 고객이 담당직원의 자료를 보고 싶을 때 즉, 고객명을 입력하면  담당직원 자료 출력  
        :    ~ WHERE GOGEK_NAME='강나루'
출력 ==>  직원명    직급   부서명  부서전화    성별

SELECT jikwonname AS 직원명, jikwonjik AS 직급, busername AS 부서명, busertel AS 부서전화, jikwongen AS 성별
FROM jikwon, gogek, buser 
WHERE gogekname='강나루' AND gogekdamsano=jikwonno AND busernum=buserno;

문4) 부서와 직원명을 입력하면 관리고객 자료 출력
        ~ WHERE BUSER_NAME='영업부' AND JIKWON_NAME='이순신'
출력 ==>  고객명    고객전화      성별
            강나루   123-4567       남
            
SELECT gogekname AS 고객명, gogektel AS 고객전화, case
when gogekjumin LIKE '%-1%' then '남'
when gogekjumin LIKE '%-2%' then '여' END AS 고객성별
FROM jikwon, gogek, buser
WHERE gogekdamsano=jikwonno 
AND busernum=buserno
AND busername='영업부'
AND jikwonname='이순신';

JIKWON, BUSER, GOGEK 테이블을 사용한다.
SELECT * FROM jikwon;
SELECT * FROM buser;
SELECT * FROM gogek;

문1) 2010년 이후에 입사한 남자 중 급여를 가장 많이 받는 직원은? *

SELECT jikwonname AS 직원이름 FROM jikwon 
WHERE jikwonpay = (SELECT MAX(jikwonpay) FROM jikwon WHERE jikwongen='남' AND DATE_FORMAT(jikwonibsail, '%Y') >= 2010);

SELECT jikwonname
FROM jikwon
WHERE jikwongen='남'
  AND jikwonibsail >= '2011-01-01'
  AND jikwonpay = (
        SELECT MAX(jikwonpay)
        FROM jikwon
        WHERE jikwongen='남'
          AND jikwonibsail >= '2011-01-01'
  );

문2)  평균급여보다 급여를 많이 받는 직원은? *

SELECT jikwonname AS 직원이름 FROM jikwon
WHERE jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon);

문3) '이미라' 직원의 입사 이후에 입사한 직원은? *

SELECT jikwonname AS 직원이름 FROM jikwon
WHERE jikwonibsail >= (SELECT jikwonibsail FROM jikwon WHERE jikwonname='이미라'); 

-- 동명이인이 있을 수 있으므로 jikwonno(pk)로 찾던가, limit 1로 걸어주는게 더 안전!
SELECT jikwonname AS 직원이름 FROM jikwon 
WHERE jikwonibsail > (
    SELECT jikwonibsail
    FROM jikwon
    WHERE jikwonname='이미라'
    LIMIT 1
);

문4) 2010 ~ 2015년 사이에 입사한 총무부(10),영업부(20),전산부(30) 직원 중 급여가 가장 적은 사람은? *

SELECT jikwonname AS 직원이름 FROM jikwon
WHERE DATE_FORMAT(jikwonibsail, '%Y') >= 2010 AND DATE_FORMAT(jikwonibsail, '%Y') <= 2015 AND jikwonpay = (SELECT MIN(jikwonpay) FROM jikwon 
WHERE DATE_FORMAT(jikwonibsail, '%Y') >= 2010 
AND DATE_FORMAT(jikwonibsail, '%Y') <= 2015 
AND busernum IN('10','20','30')); 채미리 최미숙  -- >괄호 안에서 4000이란 값을 뽑아내서 직원 중 4000의 연봉을 받는 사람들이 출력됨

SELECT * FROM jikwon
WHERE jikwonibsail BETWEEN '2010-1-1' AND '2015-12-31' 
AND jikwonpay = (SELECT MIN(jikwonpay) FROM jikwon WHERE jikwonibsail BETWEEN '2010-1-1' AND '2015-12-31' and busernum IN(10,20,30))
AND jikwonjik IS NOT NULL;
(직급이 NULL인 자료는 작업에서 제외)

 

문5) 한송이, 이순신과 직급이 같은 사람은 누구인가? *

SELECT jikwonname AS 직원이름 FROM jikwon
WHERE jikwonjik IN(SELECT jikwonjik FROM jikwon WHERE jikwonname='한송이' OR jikwonname='이순신');

문6) 과장 중에서 최대급여, 최소급여를 받는 사람은? -- (어렵네..)

SELECT jikwonname AS 직원이름, jikwonpay AS 급여 FROM jikwon
WHERE jikwonjik='과장'
AND (jikwonpay = (SELECT max(jikwonpay) FROM jikwon WHERE jikwonjik='과장')
OR jikwonpay= (SELECT MIN(jikwonpay) FROM jikwon WHERE jikwonjik='과장'));

SELECT jikwonname AS 직원이름, jikwonpay AS 급여 FROM jikwon WHERE jikwonjik='과장' AND
jikwonpay IN((SELECT MAX(jikwonpay) FROM jikwon WHERE jikwonjik='과장'),(SELECT MIN(jikwonpay) FROM jikwon WHERE jikwonjik='과장'));
문7) 10번 부서의 최소급여보다 많은 사람은? *

SELECT count(jikwonname) AS 직원수 FROM jikwon
WHERE jikwonpay > (SELECT MIN(jikwonpay) FROM jikwon WHERE busernum='10');

문8) 30번 부서의 평균급여보다 급여가 많은 '대리' 는 몇명인가? *

SELECT COUNT(jikwonname) AS 직원수 FROM jikwon
WHERE jikwonjik='대리' AND jikwonpay > (SELECT AVG(jikwonpay) FROM jikwon WHERE busernum=30);

문9) 고객을 확보하고 있는 직원들의 이름, 직급, 부서명을 입사일 별로 출력하라. * -- 이거도 좀 어렵다.. left outer join과 inner join의 차이 알아보기..

SELECT jikwonname AS 직원이름, jikwonjik AS 직급, busername AS 부서명, jikwonibsail AS 입사일 FROM jikwon 
INNER JOIN buser ON busernum=buserno
WHERE jikwonno IN(SELECT gogekdamsano FROM gogek)
ORDER BY jikwonibsail ;

-- 이게 정답임
SELECT jikwonname AS 직원이름, jikwonjik AS 직급, busername AS 부서명, jikwonibsail AS 입사일 FROM jikwon 
LEFT OUTER JOIN buser ON busernum=buserno
WHERE jikwonno IN (SELECT DISTINCT gogekdamsano FROM gogek) ORDER BY jikwonibsail;

문10) 이순신과 같은 부서에 근무하는 직원과 해당 직원이 관리하는 고객 출력

SELECT jikwonname AS 직원이름, busername AS 부서명, busertel AS 부서전화, jikwonjik as 직급, gogekname as 고객명, gogektel AS 고객전화, case
when YEAR(NOW()) - (1900 + SUBSTR(gogekjumin,1,2)) <= 30 then '청년'
when YEAR(NOW()) - (1900 + SUBSTR(gogekjumin,1,2)) <= 50 then '중년'
ELSE '노년' end as 고객구분, YEAR(NOW()) - (1900 + SUBSTR(gogekjumin,1,2)) as 고객나이 FROM jikwon 
INNER JOIN buser ON busernum=buserno
INNER JOIN gogek ON gogekdamsano=jikwonno 
WHERE busernum=(SELECT busernum FROM jikwon WHERE jikwonname='이순신')
ORDER BY 고객나이 desc;
(고객은 나이가 30 이하면 '청년', 50 이하면 '중년', 그 외는 '노년'으로 표시하고, 고객 연장자 부터 출력)

출력 ==>  직원명    부서명     부서전화     직급      고객명    고객전화    고객구분

          한송이    총무부     123-1111    사원      백송이    333-3333    청년   
          
          

문1) 사번   이름    부서  직급  근무년수  고객확보

        1   홍길동  영업부 사원     6           O   or  X

조건 : 직급이 없으면 임시직, 전산부 자료는 제외

위의 결과를 위한 뷰파일 v_exam1을 작성

CREATE OR REPLACE VIEW v_exam1 AS
SELECT DISTINCT jikwonno AS 사번, jikwonname AS 이름, busername AS 부서,
nvl(jikwonjik, '임시직') AS 직급, year(NOW()) - SUBSTR(jikwonibsail,1,4) AS 근무년수,
case nvl(gogekname, 'a') 
when 'a' then 'X' ELSE 'O' END AS 고객확보 
FROM jikwon LEFT OUTER JOIN buser ON busernum=buserno LEFT OUTER JOIN gogek ON jikwonno=gogekdamsano
WHERE busername <> '전산부' OR busername IS NULL;

SELECT * FROM v_exam1;

문2) 부서명   인원수

       영업부     7

조건 : 직원수가 가장 많은 부서 출력

위의 결과를 위한 뷰파일 v_exam2을 작성

CREATE OR REPLACE VIEW v_exam2 AS
SELECT busername AS 부서명, COUNT(*) AS 인원수 FROM jikwon RIGHT OUTER JOIN buser ON busernum=buserno GROUP BY busername 
WHERE max(인원수) IN(SELECT COUNT(*) FROM jikwon GROUP BY busernum);

CREATE OR REPLACE VIEW v_exam2 AS
SELECT busername AS 부서명, COUNT(*) AS 인원수 FROM buser INNER JOIN jikwon ON buserno=busernum GROUP BY busername
HAVING COUNT(*)=(SELECT COUNT(*) FROM jikwon GROUP BY busernum ORDER BY COUNT(*) DESC LIMIT 1); -- < 이게 최대값 하나만 남기는 수식

SELECT * FROM v_exam2;
문3) 가장 많은 직원이 입사한 요일에 입사한 직원 출력

    직원명   요일     부서명   부서전화

    한국인  수요일   전산부   222-2222

위의 결과를 위한 뷰파일 v_exam3을 작성
SELECT * FROM jikwon;  
SELECT * FROM buser;  

CREATE OR REPLACE VIEW v_exam3 AS
SELECT jikwonname AS 직원명, DATE_FORMAT(jikwonibsail, '%W') AS 요일, busername AS 부서명, busertel AS 부서전화 FROM jikwon 
LEFT OUTER JOIN buser ON busernum=buserno WHERE DATE_FORMAT(jikwonibsail, '%W') = 
(SELECT DATE_FORMAT(jikwonibsail, '%W') FROM jikwon GROUP BY DATE_FORMAT(jikwonibsail, '%W') HAVING COUNT(*) = 
(SELECT COUNT(*) FROM jikwon GROUP BY DATE_FORMAT(jikwonibsail, '%W') ORDER BY COUNT(*) DESC LIMIT 1));

SELECT * FROM v_exam3;
-- 문제 2번 
ㄴ
CREATE VIEW V_EXAM2 AS
SELECT bu.busername AS 부서명, COUNT(j.jikwonno) AS 인원수
FROM buser bu
JOIN jikwon j ON bu.buserno = j.busernum
GROUP BY bu.buserno
HAVING COUNT(j.busernum) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(*) AS cnt 
        FROM jikwon 
        GROUP BY busernum
    ) AS 부서통계
)
SELECT * FROM V_EXAM2;

-- 문제 3번

CREATE VIEW V_EXAM3 AS

CREATE VIEW V_EXAM3 AS
SELECT j.jikwonname AS 직원명,
       DAYNAME(j.jikwonibsail) AS 요일,
       bu.busername AS 부서명,
       bu.busertel AS 부서전화
FROM jikwon j
JOIN buser bu ON j.busernum = bu.buserno
WHERE DAYNAME(j.jikwonibsail) IN (
    SELECT 요일명
    FROM (
        SELECT DAYNAME(jikwonibsail) AS 요일명, COUNT(*) AS 입사인원
        FROM jikwon
        GROUP BY DAYNAME(jikwonibsail)
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ) AS 최대요일
);

SELECT * FROM V_EXAM3;