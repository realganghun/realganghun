#예외처리 : 파일, 네트워크, DB작업 실행에러 등의 error 대처하기
#웬만해서 쓰는게 좋음(error났을때 수정이 빠름), 왠지 느낌이 싸할때 걸어주기
def divide(a,b):
    return a/b

#--------------------------이런 저런 작업 진행--------------------------
#c = divide(5, 2) --> 정상실행
#c = divide(5, 0) --> error발생!
#print(c)

try : #실행문(예외 발생 가능 구문)
    c = divide(5, 2)
    print(c)

    #aa = [1, 2]
    #print(aa[0], aa[3])

    open('c:/work/abc.txt')
except ZeroDivisionError: #예외 종류 관련 클래스
    print('두번째 값은 0을 주면 안됨') #예외 발생 처리 구문
except IndexError as idxerr: #<-- 이런식으로 별명을 줄 수도 있음
    print('aa는 0, 1번의 index만 존재함. 원인 : ', idxerr)
except Exception as e: #모든 error를 하나의 exception으로 해결할 수 있다!!
    print('에러 발생 원인 : ', e)
finally : #error발생하던 안하던 무조건 통과하는 구간
    print('에러 유무에 상관없이 반드시 수행됨')

print('end')
print('aaaaaa')