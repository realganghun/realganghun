#matplotlib : 그래프 생성을 위한 다양한 함수를 제공하는 plotting library
#시각화의 중요성

import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='malgun gothic') #이래야 한글 안깨짐
plt.rcParams['axes.unicode_minus'] = False

x = ["서울", "인천", "수원"] #list type 잘 출력됨.
# x = ("서울", "인천", "수원") #tuple type 잘 출력됨
# x = {"서울", "인천", "수원"} #set type은 순서가 없어서 오류 발생
y = [5, 3, 7]

plt.xlim([-1, 3])
plt.ylim([0, 10])

plt.yticks(list(range(0,11,3)))
plt.plot(x, y)
plt.show()

data = np.arange(1, 11, 2)
plt.plot(data) # x축의 구간은 자동 설명
x = [0,1,2,3,4]
for a, b in zip(x,data):
    plt.text(a, b, str(b))
plt.show()

x = np.arange(0, 10, 0.5)
y = np.sin(x)


# plt.plot(x, y)
# plt.plot(x, y, 'bo')
plt.plot(x, y, 'go--', linewidth=2, markersize=12)
plt.show()

# hold : 복수의 plot으로 여러개의 차트를 겹쳐 그림
x = np.arange(0, 3 * np.pi, 0.1)
print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 5)) # 그래프 전체 크기(w, h)
plt.plot(x, y_sin, 'r') #선 그래프
plt.scatter(x, y_cos) #산점도 그래프
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('sine & cosine')
plt.legend(['sine', 'cosine']) #범례
plt.show()

print()
#subplot : 하나의 Figure를 여러개의 Axes로 나누기
plt.subplot(2, 1, 1) #2행 1열의 첫번째
plt.plot(x,y_sin)
plt.title('sine')
plt.legend('sine')
plt.subplot(2, 1, 2) #2행 1열의 두번째
plt.plot(x,y_cos)
plt.title('cosine')
plt.legend('cosine')
plt.show()

irum=['a','b','c','d','e']
kor = [80, 50, 60, 70, 90]
eng = [60, 70, 80, 60, 100]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bo--')
plt.ylim([50,100])
plt.grid(True)

fig = plt.gcf()
plt.show()
fig.savefig('plot1.png')

