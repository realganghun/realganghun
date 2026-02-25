문제1) 5년 이상 근무하면 '감사합니다', 그 외는 '열심히' 라고 표현 ( 2010 년 이후 직원만 참여 )

        특별수당(pay를 기준) : 5년 이상 5%, 나머지 3% (정수로 표시:반올림)

출력 형태 ==>   직원명   근무년수      표현           특별수당

 

                         홍길동     11       감사합니다         150

 
SELECT * FROM jikwon;

SELECT jikwonname AS '직원명',
DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y') AS '근무년수', 
case when (DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y')) >= 10 then '감사합니다' ELSE '열심히' end AS '표현',
case when (DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y')) >= 10 then round(jikwonpay*0.05) ELSE ROUND(jikwonpay*0.03) END AS '특별수당'
FROM jikwon WHERE DATE_FORMAT(jikwonibsail, '%Y') >= 2010;

문제2) 입사 후 8년 이상이면 왕고참, 5년 이상이면 고참, 3년 이상이면 보통, 나머지는 일반으로 표현

출력==>  직원명    직급    입사년월일    구분      부서

 

          홍길동    부장    2009.1.5      왕고참    총무부


SELECT jikwonname AS '직원명', jikwonjik AS '직급', DATE_FORMAT(jikwonibsail, '%Y.%c.%e') AS '입사년월일', case
when (DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y')) >= 8 then '왕고참'
when (DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y')) >= 5 then '고참'
when (DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y')) >= 3 then '보통'
ELSE '일반' end AS '구분', case busernum
when 10 then '총무부'
when 20 then '영업부'
when 30 then '전산부'
when 40 then '관리부' END AS '부서'
FROM jikwon;

문제3) 각 부서번호별로 실적에 따라 급여를 다르게 인상하려 한다. 

     pay를 기준으로 10번은 10%, 30번은 20% 인상하고 나머지 부서는 동결한다.

     8년 이상 장기근속을 O,X로 표시

     금액은 정수만 출력(반올림)

출력==>   사번    직원명   부서    연봉    인상연봉    장기근속

               1     홍길동    10     ****      ****          O        <-- 아니면 X 표시
               
SELECT jikwonno AS '사번', jikwonname AS '직원명', busernum AS '부서', jikwonpay AS '연봉', case busernum
when 10 then round(jikwonpay*1.1)
when 30 then round(jikwonpay*1.2)
ELSE jikwonpay END AS '인상연봉', case
when(DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y')) >= 8 then 'O'
ELSE 'X' END AS '장기근속'
FROM jikwon;
