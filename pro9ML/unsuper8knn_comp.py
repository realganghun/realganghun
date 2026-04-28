# 지도학습(KNN) / 비지도학습(K-Means) 비교 - iris dataset
import numpy as np

from sklearn.datasets import load_iris
iris_data = load_iris()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris_data['data'], iris_data['target'], test_size=0.25, random_state=42)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (112, 4) (38, 4) (112,) (38,)

print('지도학습 - KNN 사용')
from sklearn.neighbors import KNeighborsClassifier
knnModel = KNeighborsClassifier(n_neighbors=3, weights='distance', metric='euclidean')
knnModel.fit(x_train, y_train)

# 예측 및 성능 확인(acc)
from sklearn import metrics
pred_label = knnModel.predict(x_test)
print('예측값 : ', pred_label[:10])     # [1 0 2 1 1 0 1 2 1 1]
print('실제값 : ', y_test[:10])         # [1 0 2 1 1 0 1 2 1 1]
print('분류 정확도 : ', metrics.accuracy_score(y_test, pred_label)) # 분류 정확도 :  1.0

# 새로운 값으로 분류해보기
knn_input = np.array([[6.1, 2.8, 4.7, 1.2]])
knn_pred = knnModel.predict(knn_input)
print(f"새로운 값은 {knn_pred}로 분류됨.")

# 새로운 값은 몇번째 자료와 거리를 확인했을까?
dist, index = knnModel.kneighbors(knn_input)
print(dist, index) # [[0.2236068  0.3        0.43588989]] [[71 82 31]] 
# k=3 이므로 71, 82, 31번 자료가 분류에 참여
# 각 점들과 떨어진 거리, 각 점들의 index가 출력됨.


print('\n비지도학습 - K-Means 사용')
from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters=3, init='k-means++', random_state=0)
kmeansModel.fit(x_train)    # label이 주어지지 않는다.
print('예측 군집값 : ', kmeansModel.labels_[:10]) # 군집 라벨 출력
print()

# 군집별 자료보기
print('0 cluster : ', y_train[kmeansModel.labels_ == 0])    # 0번째 군집은 라벨2(virginica)
print('1 cluster : ', y_train[kmeansModel.labels_ == 1])    # 1번째 군집은 라벨0(setosa)
print('2 cluster : ', y_train[kmeansModel.labels_ == 2])    # 2번째 군집은 라벨1(versicolor)

# 새로운 값 군집 분류
new_input = np.array([[6.1, 2.8, 4.7, 1.2]])
clu_pred = kmeansModel.predict(new_input)
print(f"새로운 값은 {clu_pred}로 분류됨.")

# 군집 모델 성능 파악
pred_cluster = kmeansModel.predict(x_test)
print('pred_cluster : ', pred_cluster[:10])
print('실제값 : ', y_test[:10])

# 평가 데이터를 적용해 예측한 군집을 각 iris의 종류를 의미하는 라벨값으로 다시 바꿔줘야 실제 라벨과 비교해 성능 측정 가능
np_arr = np.array(pred_cluster)
print('np_arr : ', np_arr)
np_arr[np_arr == 0], np_arr[np_arr == 1], np_arr[np_arr == 2] = 3, 4, 5 # 임시 저장
np_arr[np_arr == 3] = 2 # 군집 3(0)을 2로 라벨링함.
np_arr[np_arr == 4] = 0 # 군집 4(1)을 0으로 라벨링함.
np_arr[np_arr == 5] = 1 # 군집 5(2)을 1로 라벨링함.

print('np_arr 재라벨링 : ', np_arr[:10])    # [1 0 2 1 1 0 1 2 1 1]
print('실제값 : ', y_test[:10])             # [1 0 2 1 1 0 1 2 1 1]

predict_label = np_arr.tolist()
print(predict_label)
print(f'군집 test acc : {np.mean(predict_label == y_test)}') # 0.9473684210526315