# SVM 분류 모델로 이미지 분류
# 세계 정치인들 중 일부 얼굴사진 데이터 사용
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import numpy as np

faces = fetch_lfw_people(min_faces_per_person=60, color=False, resize=0.5)
# 한 사람 당 60장 이상의 사진이 있는 자료만 사용
# print(faces)
# print(faces.DESCR)
print(faces.data)
print(faces.data.shape) # (1348, 2914)
print(faces.target) # [1 3 3 ... 7 3 5]
print(faces.target_names) 
# ['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush'
#  'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
print(faces.images.shape) # (1348, 62, 47)

print()
print(faces.images[1])
print(faces.target_names[faces.target[1]])

# plt.imshow(faces.images[1], cmap='bone') # 이미지 1개 시각화
# plt.show()

fig, ax = plt.subplots(3,5) # 원본 이미지 15개 시각화
for i, axi in enumerate(ax.flat):
    axi.imshow(faces.images[i], cmap='bone')
    axi.set(xticks=[], yticks=[], xlabel=faces.target_names[faces.target[i]])
plt.show()

# 주성분 분석으로 이미지 차원 축소시켜 분류 작업 진행 ------------------
# 설명력 95%되는 최소 개수를 얻기
pca = PCA(n_components=0.95)
x_pca = pca.fit_transform(faces.data)
print('pca.n_components_ : ', pca.n_components_) # pca.n_components_ :  184

n = 100 # 차원 수는 분석가가 결과를 보고 판단함.
m_pca = PCA(n_components=n, whiten=True, random_state=0)
# whiten=True : 주성분의 스케일이 작아지도록 조정
x_low = m_pca.fit_transform(faces.data) # (1348, 2914) -> (1348, n)
print('x_low : ', x_low, ' ', x_low.shape) #(1348, 150)

fig, ax = plt.subplots(3,5, figsize=(5, 4)) # 이미지 15개 시각화
for i, axi in enumerate(ax.flat):
    axi.imshow(m_pca.components_[i].reshape(faces.images[0].shape), cmap='bone')
    # reshape(faces.images[0].shape) : [2914] -> [62, 47]
    axi.axis('off')
    axi.set_title(f'PC {i+1}')
plt.suptitle('Eigenfaces(주성분 얼굴)', fontsize=12)
plt.tight_layout()
plt.show() # 출력 이미지는 실제 얼굴이 아니라 특징 패턴(얼굴 윤곽, 눈 위치, 코 그림자... 등)을 보여줌
# SVM 알고리즘은 실제 얼굴이 아니라 특징 패턴으로 분류작업을 함
# 설명력 : 

print('****설명력 확인****'*8)
print(m_pca.explained_variance_ratio_[:10])
print('누적 설명력 : ', m_pca.explained_variance_ratio_.sum()) # 누적 설명력 :  0.9039585
# n개로 얼마나 원본 정보를 유지했는지 확인함

# 원본 vs 복원 이미지 비교
x_reconst = m_pca.inverse_transform(x_low)
fig, ax = plt.subplots(2, 5, figsize=(10, 4))
for i in range(5):
    # 원본
    ax[0, i].imshow(faces.images[i], cmap='bone')
    ax[0, i].set_title("원본")
    ax[0, i].axis('off')

    # 복원
    ax[1, i].imshow(
        x_reconst[i].reshape(faces.images[0].shape), cmap='bone'
    )
    ax[1, i].set_title("복원")
    ax[1, i].axis('off')

plt.suptitle('PCA 복원 비교', fontsize=12)
plt.tight_layout()
plt.show() # 원본과 복원된 이미지의 기본 특징은 크게 차이가 없다. (패턴이 유지됨, 컴퓨터의 입장에서.)

print()
# 분류 모델 생성
svc_model = SVC(C=1.0, random_state=1)
mymodel = make_pipeline(m_pca, svc_model) # PCA와 분류기를 하나의 파이프라인으로 묶어 순차적으로 실행
print('mymodel : ', mymodel)
# mymodel :  Pipeline(steps=[('pca', PCA(n_components=100, random_state=0, whiten=True)),
#                 ('svc', SVC(random_state=1))])

# train / test split
x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state=1, stratify=faces.target) #stratify : 불균형 자료 완화
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (1011, 2914) (337, 2914) (1011,) (337,)
print(x_train[0]) # [0.04052288 0.03006536 0.09803922 ... 0.76862746 0.7647059  0.793464  ]
print(y_train[0]) # 3 <- 'George W Bush'

mymodel.fit(x_train, y_train)
pred = mymodel.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10])
# 예측값 :  [3 3 4 3 3 0 7 3 3 1]
# 실제값 :  [3 5 4 2 4 0 6 3 3 1]

# 정확도
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
confmat = confusion_matrix(y_test, pred)
print('confusion_matrix : \n', confmat)
# [[ 12   1   0   6   0   0   0   0]
#  [  0  50   0   9   0   0   0   0]
#  [  0   1  15  14   0   0   0   0]
#  [  0   0   0 133   0   0   0   0]
#  [  0   0   0  12  14   0   0   1]
#  [  0   1   0   7   1   9   0   0]
#  [  0   0   0   3   0   0  11   1]
#  [  0   1   0   7   0   0   0  28]]
print('정확도 : ', accuracy_score(y_test, pred)) #정확도 :  0.8071216617210683
print('classification_report : \n', classification_report(y_test, pred, target_names=faces.target_names))
#                     precision    recall  f1-score   support

#      Ariel Sharon       1.00      0.63      0.77        19
#      Colin Powell       0.93      0.85      0.88        59
#   Donald Rumsfeld       1.00      0.50      0.67        30
#     George W Bush       0.70      1.00      0.82       133
# Gerhard Schroeder       0.93      0.52      0.67        27
#       Hugo Chavez       1.00      0.50      0.67        18
# Junichiro Koizumi       1.00      0.73      0.85        15
#        Tony Blair       0.93      0.78      0.85        36

#          accuracy                           0.81       337
#         macro avg       0.94      0.69      0.77       337
#      weighted avg       0.85      0.81      0.80       337

print('*******분류 결과 시각화********'*6)
# x_test[0] 번째 1개만 보기
# plt.subplots(1,1)
# plt.imshow(x_test[0].reshape(62,47), cmap='bone') # 1차원 -> 2차원으로 변환
# plt.show()

# 여러개 보기
fig, axes = plt.subplots(4, 6)
for i, ax in enumerate(axes.flat):
    ax.imshow(x_test[i].reshape(62, 47), cmap='bone')
    ax.set(xticks=[], yticks=[])
    ax.set_ylabel(faces.target_names[pred[i]].split()[-1], color = 'blue' if pred[i]==y_test[i] else 'red', \
                fontweight='bold') # Last name만 취하기!!

fig.suptitle('예측 결과', fontsize=12)
plt.tight_layout()
plt.show()

# 오차 행렬 시각화 - heatmap 사용
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(confmat, annot=True, fmt='d', cmap='Blues', xticklabels=faces.target_names, yticklabels=faces.target_names)
plt.xlabel('예측')
plt.ylabel('실제')
plt.title('Confusion matrix')
plt.tight_layout()
plt.show()

# PCA 누적 분산 그래프 (왜 n_components=n인가?)
plt.plot(np.cumsum(m_pca.explained_variance_ratio_))
plt.xlabel('주성분 개수')
plt.ylabel('누적 설명력')
plt.title('PCA 설명력')
plt.grid()
plt.show()

print('-------------새로운 이미지를 입력해 분류하기-----------'*5)
# 현재 모델의 분류 accuracy : 0.8071216617210683
# 실습 1 : 기존 데이터로 테스트
test_img = faces.data[0].reshape(1, -1) # (1, 2914) 형태로 변환해야 함!!!
print('test_img : ', test_img)
test_pred = mymodel.predict(test_img)
print('실습 1 예측 결과 : ', faces.target_names[test_pred[0]], ', index : ', test_pred[0])
print('실제값 : ', faces.target_names[faces.target[0]], ', index : ', faces.target[0])
# 실습 1 예측 결과 :  Colin Powell , index :  1
# 실제값 :  Colin Powell , index :  1

print()
# 실습 2: 새로운 데이터로 분류하기
# 단계 : 이미지 읽기 -> 흑백변환 -> 크기 맞추기(62x47) -> 1차원으로 변환 -> 예측
from PIL import Image

img = Image.open('George_W_Bush.jpeg') # 이미지 읽기
img = img.convert('L') # img를 흑백으로 변환
img = img.resize((47, 62)) # resize
# numpy 이미지는 (height, width) - 세로, 가로
# PIL 이미지는 (width, height) - 가로, 세로. 이미지는 라이브러리마다 축 순서가 다름.
img_np = np.array(img) # numpy변환
# print('img_np : ', img_np, ' ', img_np.shape) #(673, 559)
img_np = img_np / 255.0 # 정규화 (학습 데이터와 scale을 맞추기 위해)
# print(img_np)
img_flat = img_np.reshape(1, -1) # 1차원으로 변환

# 예측 : 
new_pred = mymodel.predict(img_flat)
print('실습2 예측 결과 : ', faces.target_names[new_pred[0]], ', index : ', new_pred[0])

# 시각화 + 예측
plt.imshow(img_np, cmap='bone')
plt.title(f"예측 : {faces.target_names[new_pred[0]]}")
plt.axis('off')
plt.show()
# 참고 : 정확도를 높이려면 밝기/위치 정렬 등의 작업이 필요함.