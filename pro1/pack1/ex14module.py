# Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리
# 하나의 파일은 하나의 모듈이 됨
# 표준 모듈, 사용자 작성 모듈, 제 3자 모듈(third party)로 구분 

print(print.__module__) #builtins <- 이 모듈 안에 들어있다는 뜻

#----------------------------뭔가 하다가 외부 모듈 사용하기-----------------------------------------
import sys

print(sys.path)
# ['C:\\work\\projects\\pro1\\pack1', 'C:\\Users\\gs156\\anaconda3\\envs\\myproject\\python313.zip', 'C:\\Users\\gs156\\anaconda3\\envs\\myproject\\DLLs', 'C:\\Users\\gs156\\anaconda3\\envs\\myproject\\Lib', 'C:\\Users\\gs156\\anaconda3\\envs\\myproject', 'C:\\Users\\gs156\\anaconda3\\envs\\myproject\\Lib\\site-packages']
# 여기 있는 애들만 import가 가능하다는 뜻
a = 5

if a > 7:
    sys.exit() # ---> 응용 프로그램 강제 종료
import math
print(math.pi)

import calendar
calendar.setfirstweekday(6) #6이 일요일
calendar.prmonth(2026,2)
del calendar

import random #상수는 대문자, 변수는 소문자
print(random.random())
print(random.randrange(1,10))

from random import random, choice, randrange #from (모듈) import (모듈의 멤버)
from random import * #random의 모든 멤버를 쓰겠다. 근데 메모리 아끼려면 윗 방법이 낫다.
print(random())
print(randrange(1,100))

print('end')