#----------------------------------사용자 정의 모듈 처리하기----------------------------------------------
#C:\work\projects\pro1\pack1\ex15module2 - main

s = 20

#---------------------------------경로 지정 방법1 : import 모듈명-----------------------------------------
import pack1.mymod1
print(dir(pack1.mymod1))
print(pack1.mymod1.__file__)
print(pack1.mymod1.__name__)

list1 = [1,2]
list2 = [3,4,5]

pack1.mymod1.listHap(list1, list2)

if __name__ == '__main__':
    print('메인모듈')

#--------------------------------경로 지정 방법2 : from 모듈명 import 함수명 또는 변수--------------------------
from pack1.mymod1 import kbs #ctrl + spacebar누르면 멤버가 나옴
kbs()
from pack1.mymod1 import mbc, tot
mbc()
print(tot)
from pack1.mymod1 import * #*을 사용해 mymod1 모듈의 모든 멤버를 불러옴, 권장사항은 아님

from pack1.mymod1 import mbc as 엠비씨만세별명
엠비씨만세별명()
#-------------------------------경로 지정 방법3: import 하위패키지.모듈명-------------------------
import pack1.subpack.sbs
pack1.subpack.sbs.sbsMansae()

import pack1.subpack.sbs as nickname
nickname.sbsMansae()
#-----------------------------경로 지정 방법4: 현재 package와 동등한 다른 패키지 모듈 읽기-------------------------
#--> 바로 못가서 돌아서 가야함, 명령어 : (myproject) C:\work\projects\pro1>python -m pack1.ex15module2

# import ../pack1_other.mymod2 --> VScode는 이 구조를 인정 X
from pack1_other import mymod2
kk = mymod2.hapFunc(4, 3)
print(kk)

import mymod3
result = mymod3.gopFunc(4, 3) #<- path가 설정된 곳의 module읽기
print(result)