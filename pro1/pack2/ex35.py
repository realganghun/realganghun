#with 구문 사용 - 내부적으로 close()를 해줌

try:
    #파일 저장
    with open('ftext3.txt', mode = 'w', encoding='utf-8') as fobj1:
        fobj1.write('파이썬에서 문서저장\n')
        fobj1.write('with 구문은 \n')
        fobj1.write('명시적으로 close()할 필요 없음')
    print('저장완료')

    with open('ftext3.txt', mode='r', encoding='utf-8') as fobj2:
        print(fobj2.read())
    
    
    print('\n\n피클링(일반 객체 및 복합 객체 파일 처리)')
    import pickle

    dictData = {'tom' : '111-1111', '길동' : '222-2222'}
    listData = ['마우스', '키보드']
    tupleData = (dictData, listData)
    
    with open('hello.dat', mode='wb') as fobj3:
        pickle.dump(tupleData, fobj3) #pickle.dump(대상, 파일객체)
        pickle.dump(listData, fobj3) #list type 객체만 저장
    print('특정 객체를 파일로 저장')
    
    print('피클 객체 읽기')
    with open('hello.dat', mode = 'rb') as fobj4:
        a, b = pickle.load(fobj4) #pickle.load() <--- 읽을 때
        print('a :', a)
        print('b :', b)
        c = pickle.load(fobj4)
        print('c :', c)
except Exception as e:
    print('err : ', e)