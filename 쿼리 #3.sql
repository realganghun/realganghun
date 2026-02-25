CREATE TABLE prof(profcode INT PRIMARY KEY, profname CHAR(10), lab INT CHECK(100 <= lab <= 500));
SELECT * FROM prof;

CREATE TABLE subj(subjcode INT PRIMARY KEY AUTO_INCREMENT, subjname CHAR(10) NOT NULL UNIQUE, bookname CHAR(10), profname INT, FOREIGN KEY(profname) REFERENCES prof(profcode));
SELECT * FROM subj;

CREATE TABLE stu(stucode INT PRIMARY KEY, stuname CHAR(10), sub INT, FOREIGN KEY(sub) REFERENCES subj(subjcode), stugrade INT DEFAULT 1 CHECK(1 <= stugrade <= 4));
SELECT * FROM stu;

DROP TABLE subj;