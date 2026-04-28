[문항1] TRUNCATE TABLE 말고 테이블을 삭제하는 일반적인 명령어 형식을 적으시오.
(배점:5)

drop table <테이블명>;


[문항2] 외래키가 참조하는 대상은 무엇인가요?
(배점:5)

다른 테이블의 column

	
[문항3] 그룹화 후 조건을 지정하는 명령어는 무엇인가요?
(배점:5)

group by <column명> having <조건>
	
[문항4] 다음 DDL 문에서 pay의 입력 값을 2000 이상만 입력할 수 있도록 제약 조건을 기술하시오.
create table emp (eno INT PRIMARY KEY, ename varchar(10), job varchar(9), pay int ______________________________ );
(배점:5)

CHECK(pay >= 2000)
	
[문항5] MariaDB에서 WHERE 절을 생략하고 UPDATE 문을 실행하면 어떤 일이 발생하는가?
(배점:5)

모든 record의 해당 column값이 수정값으로 바뀌게 된다.
	
[문항6] 테이블 생성 시 부여하는 제약 조건의 종류를 아는 대로 3개 이상 기술하시오.
(배점:5)

기본키 제약(primary key)
check 제약
unique 제약
foreign key 제약

[문항7] buser 테이블에서 buserno(부서번호)가 3인 데이터(레코드)를 삭제하는 SQL 구문을 작성하시오.
(배점:5)

DELETE FROM buser WHERE buserno=3;

[문항8] MariaDB에서 NULL 값과 비교할 때 = 연산자를 사용할 수 없다. 그러면 가능한 연산자는 무엇인가?
(배점:5)

IS
	
[문항9] jikwon 테이블과 buser 테이블을 이용하여 직급이 '과장'인 직원만 조회하는 query문을 작성하시오.
조건 : join 사용
출력 형태 예:
  jikwonno  jikwonname  busername  jikwonjik
        3              이순신            영업부            과장
  ...
(배점:5)

SELECT jikwonno, jikwonname, busername, jikwonjik FROM jikwon INNER JOIN buser ON busernum=buserno WHERE jikwonjik='과장';

[문항10] MariaDB 문자 자료형에서 char과 VARCHAR의 차이점을 간단히 설명하시오.
(배점:5)

char은 고정길이 문자형
varchar는 가변길이 문자형

[문항11] jikwon 테이블에서 연봉이 5000 이상이고 7000 이하인 직원을 검색하여 직원번호, 직원명, 연봉을 출력하는 SQL문을 두 가지 방법(and, between)으로 작성하시오.
(배점:10)

SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonpay >= 5000 AND jikwonpay <=7000;
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonpay BETWEEN 5000 and 7000;
	
[문항12] jikwon 테이블을 사용하여 평균 연봉보다 연봉이 높은 직원들을 모두 출력하는 select 문(sub query)을 작성하시오. 칼럼은 모두 출력.
(배점:10)

SELECT * FROM jikwon WHERE jikwonpay >(SELECT AVG(jikwonpay) FROM jikwon);
	
[문항13] 아래 두 개의 ERD를 보고 테이블 생성을 위한 DDL문을 MariaDB 형식에 맞게 작성하시오.
(배점:10)

customers          ----------        orders
==================================
pk  cno  : 정수                            pk  ono : 정수 
---------------------------------------------------------
    cname : 고정문자(10)          odate : 날짜시간
    caddress : 가변문자(50)      oaddress : 가변문자(50)
    cemail  : 고정문자(20)        ophone : 가변문자(20)
    cphone : 가변문자(20)        ostatus : 가변문자(10)
                                                  ono_cus : fk
==================================
CREATE TABLE jikwon(bun INT PRIMARY KEY, irum CHAR(10) NOT NULL, buser CHAR(10) NOT NULL);
CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10) NOT NULL, birth DATETIME, jikwonbun INT, FOREIGN KEY(jikwonbun) REFERENCES jikwon(bun));

CREATE TABLE customers(cno INT PRIMARY KEY, cname CHAR(10), caddress VARCHAR(50), cemail CHAR(20), cphone VARCHAR(20));
DESC customers;
CREATE TABLE orders(ono INT PRIMARY KEY, odate DATETIME, oaddress VARCHAR(50), ophone VARCHAR(20), 
ostatus VARCHAR(10), ono_cus INT, FOREIGN KEY(ono_cus) REFERENCES customers(cno));
DESC orders;
[문항14] jikwon 테이블을 사용하기로 한다.
2015 ~ 2020 년 사이에 입사한 직원을 대상으로 년도별 인원수와 연봉평균을 출력하는 DML문을 기술하시오.
(배점:10)
SELECT * FROM jikwon;
SELECT substr(jikwonibsail,1,4) AS 입사년도, COUNT(*) AS 인원수, AVG(jikwonpay) AS 연봉평균 FROM jikwon WHERE substr(jikwonibsail,1,4) BETWEEN 2015 AND 2020 GROUP BY substr(jikwonibsail,1,4);
	
[문항15] jikwon, gogek 테이블을 사용해 '평균 급여보다 급여가 높은 직원과 그 직원이 담당하는 고객 수'를 조회하는 SELECT 문을 작성하시오.
출력: 직원명 급여 고객수
예)
직원명  급여  고객수
홍길동  9900    1
한송이  8800    3
김부만  8600    0
한국인  8000    0
이순신  7900    3
...
이유라  5500    0

건수 : 12

힌트: join, subquery, group by 등 사용
(배점:10)
SELECT jikwonname AS 직원명, jikwonpay AS 급여, COUNT(gogekno) AS 고객수 FROM jikwon LEFT OUTER JOIN gogek ON gogekdamsano=jikwonno 
WHERE jikwonpay > (select avg(jikwonpay) from jikwon) GROUP BY jikwonname ORDER BY jikwonpay DESC;

select jikwonno as 직원번호, jikwonname as 직원명, count(gogekno) as 관리고객수 from jikwon inner join gogek on gogekdamsano=jikwonno GROUP BY jikwonno;


CREATE DATABASE IF NOT EXISTS ai_quant
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_unicode_ci;

USE ai_quant;

-- 1. 사용자
CREATE TABLE users (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nickname VARCHAR(100) NOT NULL,
    is_verified TINYINT(1) NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_users_email (email),
    UNIQUE KEY uk_users_nickname (nickname)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

DESC users;
-- 2. 모의투자 계좌
CREATE TABLE mock_accounts (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id BIGINT UNSIGNED NOT NULL,
    initial_balance DECIMAL(15,2) NOT NULL DEFAULT 10000000.00,
    current_balance DECIMAL(15,2) NOT NULL DEFAULT 10000000.00,
    total_profit_loss DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_mock_accounts_user_id (user_id),
    CONSTRAINT fk_mock_accounts_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. 주식 기본 정보
CREATE TABLE stocks (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    ticker VARCHAR(30) NOT NULL,
    name_kr VARCHAR(100) NOT NULL,
    market VARCHAR(30) NOT NULL,
    sector VARCHAR(50) DEFAULT NULL,
    is_defense TINYINT(1) NOT NULL DEFAULT 0,
    description TEXT DEFAULT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_stocks_ticker (ticker),
    KEY idx_stocks_is_defense (is_defense),
    KEY idx_stocks_market (market)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. 주식 상세/최신 시세
CREATE TABLE stock_details (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    stock_id BIGINT UNSIGNED NOT NULL,
    current_price DECIMAL(15,2) NOT NULL,
    change_amount DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    change_rate DECIMAL(8,2) NOT NULL DEFAULT 0.00,
    volume BIGINT UNSIGNED NOT NULL DEFAULT 0,
    market_cap BIGINT UNSIGNED DEFAULT NULL,
    per_value DECIMAL(10,2) DEFAULT NULL,
    pbr_value DECIMAL(10,2) DEFAULT NULL,
    high_price DECIMAL(15,2) DEFAULT NULL,
    low_price DECIMAL(15,2) DEFAULT NULL,
    open_price DECIMAL(15,2) DEFAULT NULL,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_stock_details_stock_id (stock_id),
    CONSTRAINT fk_stock_details_stock
        FOREIGN KEY (stock_id) REFERENCES stocks(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. 주식 히스토리
CREATE TABLE stock_price_history (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    stock_id BIGINT UNSIGNED NOT NULL,
    price_date DATE NOT NULL,
    open_price DECIMAL(15,2) NOT NULL,
    high_price DECIMAL(15,2) NOT NULL,
    low_price DECIMAL(15,2) NOT NULL,
    close_price DECIMAL(15,2) NOT NULL,
    volume BIGINT UNSIGNED NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_stock_price_history (stock_id, price_date),
    KEY idx_stock_price_history_date (price_date),
    CONSTRAINT fk_stock_price_history_stock
        FOREIGN KEY (stock_id) REFERENCES stocks(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. 거래내역
CREATE TABLE trades (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id BIGINT UNSIGNED NOT NULL,
    account_id BIGINT UNSIGNED NOT NULL,
    stock_id BIGINT UNSIGNED NOT NULL,
    trade_type ENUM('BUY', 'SELL') NOT NULL,
    price DECIMAL(15,2) NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    total_amount DECIMAL(15,2) NOT NULL,
    strategy VARCHAR(100) DEFAULT NULL,
    traded_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_trades_user_id (user_id),
    KEY idx_trades_account_id (account_id),
    KEY idx_trades_stock_id (stock_id),
    KEY idx_trades_traded_at (traded_at),
    CONSTRAINT fk_trades_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_trades_account
        FOREIGN KEY (account_id) REFERENCES mock_accounts(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_trades_stock
        FOREIGN KEY (stock_id) REFERENCES stocks(id)
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 6. 현재 보유 종목
CREATE TABLE portfolio_holdings (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id BIGINT UNSIGNED NOT NULL,
    account_id BIGINT UNSIGNED NOT NULL,
    stock_id BIGINT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL DEFAULT 0,
    avg_buy_price DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    total_invested DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uk_portfolio_user_stock (user_id, stock_id),
    KEY idx_portfolio_account_id (account_id),
    CONSTRAINT fk_portfolio_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_portfolio_account
        FOREIGN KEY (account_id) REFERENCES mock_accounts(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_portfolio_stock
        FOREIGN KEY (stock_id) REFERENCES stocks(id)
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 7. 뉴스
CREATE TABLE news (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(300) NOT NULL,
    summary TEXT DEFAULT NULL,
    content LONGTEXT DEFAULT NULL,
    source VARCHAR(100) NOT NULL,
    source_url VARCHAR(500) DEFAULT NULL,
    thumbnail_url VARCHAR(500) DEFAULT NULL,
    view_count INT UNSIGNED NOT NULL DEFAULT 0,
    published_at DATETIME NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_news_view_count (view_count),
    KEY idx_news_published_at (published_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 8. 뉴스 AI 분석
CREATE TABLE news_analysis (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    news_id BIGINT UNSIGNED NOT NULL,
    stock_id BIGINT UNSIGNED DEFAULT NULL,
    ai_score DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    sentiment ENUM('POSITIVE', 'NEUTRAL', 'NEGATIVE') NOT NULL DEFAULT 'NEUTRAL',
    ai_summary TEXT DEFAULT NULL,
    keywords VARCHAR(500) DEFAULT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_news_analysis_stock_id (stock_id),
    CONSTRAINT fk_news_analysis_news
        FOREIGN KEY (news_id) REFERENCES news(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_news_analysis_stock
        FOREIGN KEY (stock_id) REFERENCES stocks(id)
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=UTF8MB4_UNICODE_CI;

CREATE TABLE stock_news (
    stock_id BIGINT UNSIGNED NOT NULL,
    score INT NOT NULL,
    ai_summary TEXT,
    news_data JSON,  
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (stock_id),
    CONSTRAINT fk_stock_news_stock 
        FOREIGN KEY (stock_id) REFERENCES stocks(id) 
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT INTO stocks (ticker, name_kr, market, sector, is_defense, description) VALUES
('064350','현대로템','KOSPI','defense',1,'방산 및 철도 차량 제작 기업'),
('012450','한화에어로스페이스','KOSPI','defense',1,'항공엔진 및 방산 시스템 기업'),
('079550','LIG넥스원','KOSPI','defense',1,'유도무기 및 방위 시스템 개발'),
('272210','한화시스템','KOSPI','defense',1,'방산 전자 및 ICT 시스템 기업'),
('047810','한국항공우주','KOSPI','defense',1,'군용 항공기 및 항공우주 개발'),
('077970','STX엔진','KOSPI','defense',1,'선박 및 방산용 엔진 제조'),
('024740','한일단조','KOSDAQ','defense',1,'단조 부품 및 방산 부품 생산'),
('038060','루멘스','KOSDAQ','defense',1,'LED 및 전자 부품 제조'),
('007120','미래아이앤지','KOSDAQ','defense',1,'IT 및 시스템 통합 기업'),
('032820','우리기술','KOSDAQ','defense',1,'원전 및 방산 제어 시스템'),
('368770','파이버프로','KOSDAQ','defense',1,'광섬유 기반 센서 및 방산 기술'),
('230980','비유테크놀러지','KOSDAQ','defense',1,'IT 및 기술 서비스 기업'),
('009540','HD한국조선해양','KOSPI','defense',1,'조선 및 해양 방산 관련 기업'),
('003570','SNT다이내믹스','KOSPI','defense',1,'방산용 변속기 및 기계 부품'),
('005810','풍산홀딩스','KOSPI','defense',1,'풍산 그룹 지주사'),
('108380','대양전기공업','KOSDAQ','defense',1,'선박 및 방산 전기 시스템'),
('372910','한컴라이프케어','KOSDAQ','defense',1,'방독면 및 안전 장비 제조'),
('006050','국영지앤엠','KOSDAQ','defense',1,'특수 유리 및 방산 소재'),
('095190','이엠코리아','KOSDAQ','defense',1,'기계 및 방산 부품 제조'),
('042660','한화오션','KOSPI','defense',1,'잠수함 및 군함 건조'),
('010820','퍼스텍','KOSDAQ','defense',1,'방산 전자 및 무기 시스템'),
('015710','코콤','KOSDAQ','defense',1,'보안 및 통신 장비 제조'),
('013810','스페코','KOSDAQ','defense',1,'방산 및 중장비 제조'),
('040300','YTN','KOSDAQ','defense',1,'보도 전문 방송사'),
('003010','혜인','KOSPI','defense',1,'중장비 및 산업 장비 유통'),
('274090','켄코아에어로스페이스','KOSDAQ','defense',1,'항공기 부품 제조'),
('119500','포메탈','KOSDAQ','defense',1,'단조 및 기계 부품 제조'),
('035460','기산텔레콤','KOSDAQ','defense',1,'통신 장비 및 네트워크 장비'),
('361390','제노코','KOSDAQ','defense',1,'우주 및 방산 전자 시스템'),
('064960','SNT모티브','KOSPI','defense',1,'자동차 및 방산 부품'),
('096630','에스코넥','KOSDAQ','defense',1,'전자 부품 제조'),
('377330','이지트로닉스','KOSDAQ','defense',1,'전력 변환 및 전자 기술'),
('065950','웰크론','KOSDAQ','defense',1,'특수 섬유 및 방산 소재'),
('095270','웨이브일렉트로','KOSDAQ','defense',1,'RF 및 통신 장비'),
('042370','비츠로테크','KOSDAQ','defense',1,'전력 및 방산 기술 기업'),
('103140','풍산','KOSPI','defense',1,'방산 탄약 및 구리 소재'),
('010280','아이티센엔텍','KOSDAQ','defense',1,'IT 서비스 및 시스템 통합'),
('215090','솔디펜스','KOSDAQ','defense',1,'방산 장비 및 시스템'),
('000880','한화','KOSPI','defense',1,'방산 및 화학 사업 보유'),
('005870','휴니드','KOSPI','defense',1,'군용 통신 장비 제조'),
('077360','덕산하이메탈','KOSDAQ','defense',1,'전자 소재 및 부품'),
('065450','빅텍','KOSDAQ','defense',1,'군용 전자 및 방산 장비'),
('000270','기아','KOSPI','defense',1,'군용 차량 및 자동차 제조'),
('088800','에이스테크','KOSDAQ','defense',1,'통신 장비 제조'),
('003490','대한항공','KOSPI','defense',1,'항공 및 군용 항공기 정비'),
('214430','아이쓰리시스템','KOSDAQ','defense',1,'적외선 센서 및 방산 기술'),
('011210','현대위아','KOSPI','defense',1,'방산 포 및 기계 시스템'),
('068790','DMS','KOSDAQ','defense',1,'디스플레이 및 장비 제조');

INSERT INTO stock_details
(stock_id, current_price, change_amount, change_rate, volume, market_cap, per_value, pbr_value, high_price, low_price, open_price)
VALUES
(1, 820000.00, 12000.00, 1.49, 150000, 37000000000000, 24.50, 3.10, 825000.00, 801000.00, 808000.00),
(2, 245000.00, 3500.00, 1.45, 98000, 5400000000000, 18.20, 2.80, 247000.00, 239000.00, 241500.00),
(3, 98000.00, -1200.00, -1.21, 120000, 3200000000000, 14.70, 1.90, 100000.00, 97500.00, 99200.00);


SHOW TABLES;

DESC stock_price_history;

SELECT * FROM stock_price_history;
SELECT * FROM stock_details;
SELECT * FROM stocks;
DROP TABLE stocks;
DELETE FROM stocks WHERE id=1;
DELETE FROM stocks WHERE id=2;
DELETE FROM stocks WHERE id=3;

SELECT *
FROM stock_details
LIMIT 10;

SELECT name_kr, volume
FROM stock_details
JOIN stocks ON stocks.id = stock_details.stock_id
LIMIT 10;

SELECT stock_id, price_date, COUNT(*) AS cnt
FROM stock_price_history
GROUP BY stock_id, price_date
HAVING COUNT(*) > 1;

ALTER TABLE stock_price_history ADD CONSTRAINT uq_stock_price_history_stock_date UNIQUE (stock_id, price_date);
ALTER TABLE etf_price_history ADD CONSTRAINT uq_etf_price_history_etf_date UNIQUE (etf_id, price_date);


CREATE TABLE etfs (
id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
 ticker VARCHAR(30) NOT NULL,
 name_kr VARCHAR(100) NOT NULL, 
 market VARCHAR(30) NOT NULL, 
 theme VARCHAR(50) DEFAULT NULL, 
 description TEXT DEFAULT NULL,
 created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (id),
 UNIQUE KEY uk_etfs_ticker (ticker), 
 KEY idx_etfs_market (market), 
 KEY idx_etfs_theme (theme) 
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE etf_price_history (users
id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
etf_id BIGINT UNSIGNED NOT NULL, 
price_date DATE NOT NULL, 
open_price DECIMAL(15,2) NOT NULL, 
high_price DECIMAL(15,2) NOT NULL, 
low_price DECIMAL(15,2) NOT NULL, 
close_price DECIMAL(15,2) NOT NULL,
volume BIGINT UNSIGNED NOT NULL DEFAULT 0, 
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
PRIMARY KEY (id), 
UNIQUE KEY uk_etf_price_history (etf_id, price_date), 
KEY idx_etf_price_history_date (price_date), 
KEY idx_etf_price_history_etf_id (etf_id), 
CONSTRAINT fk_etf_price_history_etf 
FOREIGN KEY (etf_id) REFERENCES etfs(id) 
ON DELETE CASCADE )
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=UTF8MB4_UNICODE_CI;

INSERT INTO etfs (id, ticker, name_kr, market) VALUES (1, 463250,'tiger', 'etf');

SELECT * FROM etf_price_history;

ALTER TABLE stock_details
ADD COLUMN trading_value BIGINT;

DELETE FROM users;

DESC etf_price_history;
DESC etfs;
DESC mock_accounts;
DESC news;
DESC news_analysis;
DESC portfolio_holdings;
DESC stock_details;
DESC stock_price_history;
DESC stocks;
DESC trades;
DESC users;

SELECT * FROM stock_details;
SELECT * FROM stocks;
SELECT * FROM users;
SELECT * FROM stock_chats;

ALTER TABLE users ADD COLUMN avatar VARCHAR(10) DEFAULT '🧑‍�';


CREATE TABLE stock_chats (
id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
user_id BIGINT UNSIGNED NOT NULL,
 stock_id BIGINT UNSIGNED NOT NULL,
message TEXT NOT NULL,
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id),
CONSTRAINT fk_stock_chats_user
FOREIGN KEY (user_id) REFERENCES users(id)
ON DELETE CASCADE,
CONSTRAINT fk_stock_chats_stock
FOREIGN KEY (stock_id) REFERENCES stocks(id)
ON DELETE CASCADE
);

INSERT INTO stock_chats (user_id, stock_id, message)
VALUES
(24, 100, '오늘 거래량 괜찮은데요?'),
(25, 100, '단기 반등 가능성 있어 보여요'),
(26, 100, '뉴스 보고 들어왔어요'),
(27, 100, '이 종목은 실적 체크가 먼저인 듯'),
(28, 100, '장기적으로는 괜찮아 보입니다');

INSERT INTO stocks (id, ticker, name_kr, market, sector, is_defense)
VALUES (9999, 'DEFENSE_ALL', '방산 업종 종합', 'SECTOR', 'Defense', 1);

ALTER TABLE portfolio_holdings
    ADD COLUMN strategy VARCHAR(50) NOT NULL DEFAULT '수동 운용'
    AFTER total_invested;
    
ALTER TABLE portfolio_holdings
    ADD UNIQUE KEY uq_user_stock_strategy (user_id, stock_id, strategy);
    
ALTER TABLE portfolio_holdings
    DROP INDEX uk_portfolio_user_stock;
    
SHOW INDEX FROM portfolio_holdings;