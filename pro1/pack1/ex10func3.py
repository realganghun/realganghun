# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
def showGugu(start, end): #<-- start, end가 인수
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
        for i in range(1,10):
            print(str(dan) + "*" + \
                  str(i) + "=" + str(dan * i), end = ' ') #<-- 여기서 \는 명령을 이어간다는 뜻
        print()

showGugu(2,3)
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
def showGugu(start, end = 5):  #end = 5라는 기본값을 줌
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
        for i in range(1,10):
            print(str(dan) + "*" + \
                  str(i) + "=" + str(dan * i), end = ' ') 
        print()

showGugu(2)


# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
showGugu(start = 7, end = 9)
showGugu(end = 7, start = 5) #순서가 달라도 키워드만 대응되면 됨
showGugu(6, end = 9)
print()
#showGugu(start = 7, 9) #error 발생;;;
#showGugu(end = 7, 5) #error 발생;;;

# 가변 매개변수 : 인수의 갯수가 동적인 경우
def func1(*ar): #*ar하면 여러개의 인자를 tuple로 묶어서 받겠다
    print(ar)
    for i in ar:
        print('밥 : ' + i)

func1('김밥', '비비비비비빔~ 비 비비비빔~', '뽁')
func1('깁밥') #('깁밥',)이런 모양으로 출력됨

#-----------------------------------------------tuple-----------------------------------------------------
def func2(a, *ar):
    print(a)
    print(ar)

func2('깁밥', '비빔밥')
func2('깁밥', '비빔밥', '볶음밥', '짜장밥', '짬뽕밥', '스폰지밥')
#-------------------------------------------dict------------------------------------------------
print()
def func3(w, h, **other): # **은 dict로 받음
    print(f'몸무게 : {w}, 키 : {h}')
    print(f'기타 : {other}')

func3(1, 2, irum = 'tlsrlfn', nai = 23)
#func3(1, 2, {'irum' : 'tlsrlfn', 'nai' : 23}) #error발생
#--------------------------------------tuple&dict 연습----------------------------------
print()
def func4(a, b, *tuple, **dict):
    print(a,b)
    print(tuple)
    print(dict)

func4(1, 2, 3, 4, 5, 6, irum = '신기루', nai = 23)
#-------------------------------type hint(가독성 올리기 위해, int 안줘도 error발생 X)---------------------
def typeFunc(num : int, data : list[str]) -> dict[str,int]:
    print(num)
    print(data)
    result = {}
    for idx, item in enumerate(data, start = 8): #enumerate는 묶음형 자료에서 index를 하나씩 빼줌
        print(f'idx : {idx}, item : {item}')
        result[item] = idx
    return result

rdata = typeFunc(1, ['1', '2', '삼'])
print(rdata)