# 입력 함수 :  [사번, 이름, 기본급, 입사년도]
def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010], #list[0][0], list[0][1], list[0][2], list[0][3]
        [2, "이바다", 2200000, 2018], #list[1][0], list[1][1], list[1][2], list[1][3]
        [3, "박하늘", 3200000, 2005], #list[2][0], list[2][1], list[2][2], list[2][3]
    ]
    return datas


#급여액은 기본급 + 근속수당
#수령액은 급여액-공제액
def processfunc(datas):
    inputfunc()
    print("사번 이름 기본급 근무년수 근속수당 공제액 수령액")
    print("-------------------------------------------------------")
    count = 0
    for i in range(0,3):
        print(datas[i][0], end = ' ') #사번
        print(datas[i][1], end = ' ') #이름
        print(datas[i][2], end = ' ') #기본급
        year = 2026 - datas[i][3]
        #datetime.now().year --> 내 컴퓨터의 연도를 뽑아냄
        print(year, end = ' ') #근무년수
        gup = datas[i][2]
        gong = 0
        if year >= 9:
            print('1000000', end = ' ')
            gup += 1000000
        elif year < 9 and year >= 4:
            print('450000', end = ' ')
            gup += 450000
        elif year < 4 and year >= 0:
            print('150000', end = ' ')
            gup += 150000
        if gup >= 3000000:
            gong = int(gup * 0.5)
            print(gong, end = ' ')
        elif gup >= 2000000:
            gong = int(gup * 0.3)
            print(gong, end = ' ')
        elif gup < 2000000:
            gong = int(gup * 0.15)
            print(gong, end = ' ')
        print(gup - gong)
        count += 1
    print('처리 건수 : ', count)

datas = inputfunc()
processfunc(datas)



# 연습문제2) 리스트를 통해 상품 자료를 입력받아 가공 후 출력하기

# 처리 조건 :  
#   1) 한 개의 상품명과 가격은 문자열로 입력됨. 문자열 나누기 필요.
#   2) 취급 상품 예는 아래와 같다.
#  * 취급상품표
#   상품명   단가
#   새우깡    450
#   감자깡    300
#   양파깡,   450

# 입력 함수
def inputfunc():
    datas = [
        "새우깡,15", #comma separate value -> csv.
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas


# 처리 함수
def processfunc(datas):
    # 단가표
    price = {
        "새우깡": 450,
        "감자깡": 300,
        "양파깡": 350
    }

    
    count = {"새우깡": 0, "감자깡": 0, "양파깡": 0} # 소계용 누적 변수, dict타입
    amount = {"새우깡": 0, "감자깡": 0, "양파깡": 0}

    total_count = 0
    total_amount = 0

    print("상품명   수량   단가   금액")
    print("-----------------------------------")

    for data in datas:
        name, quantity = data.split(",")   # 문자열 분리
        quantity = int(quantity) #이거 안붙이면 string으로 처리됨
        unit = price[name]
        money = quantity * unit

        print(f"{name} {quantity} {unit} {money}")

        count[name] += quantity
        amount[name] += money
        total_count += quantity
        total_amount += money

    print("\n소계")
    for name in count:
        print(f"{name} : {count[name]}건   소계액 : {amount[name]}원")

    print("총계")
    print(f"총 건수 : {total_count}")
    print(f"총 액  : {total_amount}원")


# 실행
datas = inputfunc()
processfunc(datas)

