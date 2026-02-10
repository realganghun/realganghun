#우편정보 파일자료 읽기
#키보드에서 입력한 동이름으로 해당 주소 정보 출력

def zipProcess():
    dongIrum = input('동이름 : ')
    #dongIrum = '도곡'
    # print(dongIrum)
    with open(r'zipcode.txt', mode = 'r', encoding='euc-kr') as f:
        line = f.readline() # 한 행 읽기
        #135-806 서울    강남구  개포1동 경남아파트              1 <-- 하나의 문자열로 취급
        #print(line)
        #lines = line.split('\t') #구분자가 tab키여서 \t 사용
        #lines = line.split(chr(9)) #chr(tab에 해당하는 ascii코드)
        #print(lines)
        while line: # <-- 자료가 있으면 True, 없으면 False라는 점을 활용
            lines = line.split(chr(9))
            if lines[3].startswith(dongIrum):
                #print(lines)
                print('우편번호 : ' + lines[0] + ', ' + lines[1] + ' ' + lines[2] + ' ' + lines[3])
            line = f.readline() #<-- 이게 이해가 잘 안되네...


if __name__ == '__main__':
    zipProcess()