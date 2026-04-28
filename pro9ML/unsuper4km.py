# K-means clustering은 클러스터의 개수를 미리 정하여 반복적으로 클러스터의 평균을 업데이트하며 가장 가까운 점들을 군집화하는 방법으로, 
# clustering의 가장 기본이 되는 기법

# K-means clustering 알고리즘
# 1. 몇 개의 덩어리로 clustering할지 정한다.
# 2. 1에서 정한 개수만큼 중심점을 정한다. 
# 3. 각 점마다 가장 가까운 centroid를 정한다.
# 4. Centroid를 이동한다.
# 5. 3-4의 과정을 더 이상 새로 매핑되지 않을 때까지 반복한다.

# 그 후 새로 매핑된 점들을 바탕으로 다시 centroid를 이동한다. 
# 위의 과정을 더 이상의 이동이 없을 때까지 반복한다. 이렇게 더 이상의 이동이 없어지면, clustering이 완료되고 k개의 cluster가 생성된다.

# 실습1 - make_blobs 사용
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x, _ = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)

print(x[:3], ' ', x.shape)
plt.scatter(x[:, 0], x[:, 1], c='gray', marker='o', s=50)
plt.grid(True)
plt.show()

# k-means 모델 생성
# cluster의 중심을 선택하는 방법
# init_centroid = 'random'    # cluster의 중심을 임의로 선택
init_centroid = 'k-means++' # cluster의 중심을 k-means++로 선택, 중심을 최대한 멀리하는 방법
kmodel = KMeans(n_clusters=3, init=init_centroid, n_init=10, random_state=0)
# n_init=10 : k-means를 10번 수행한다. 가장 좋은 결과(오차 최소값)를 선택.
pred = kmodel.fit_predict(x)    # clustering으로 구분한 결과 얻기
print('pred : ', pred)

# 각 그룹별 보기
# print(x[pred == 0])
# print(x[pred == 1])
# print(x[pred == 2])
print('중심점 : ', kmodel.cluster_centers_)

# 시각화
plt.scatter(x[pred == 0, 0], x[pred == 0, 1], c='red', marker='o', s=50, label='cluster1')
plt.scatter(x[pred == 1, 0], x[pred == 1, 1], c='green', marker='s', s=50, label='cluster2')
plt.scatter(x[pred == 2, 0], x[pred == 2, 1], c='blue', marker='v', s=50, label='cluster3')
plt.scatter(kmodel.cluster_centers_[:, 0], kmodel.cluster_centers_[:, 1], c='black', marker='+', s=60, label='center') # 각 군집 중심점 표시
plt.legend()
plt.grid()
plt.show()

# kmeans의 k값은? elbow or silhoutte 기법을 이용해 k값 얻기
def elbow(x):
    sse = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i, init=init_centroid, random_state=0)
        km.fit(x)
        sse.append(km.inertia_)
    plt.plot(range(1,11), sse, marker='o')
    plt.xlabel('군집수')
    plt.ylabel('SSE')
    plt.show()

elbow(x)

'''
실루엣(silhouette) 기법
  클러스터링의 품질을 정량적으로 계산해 주는 방법이다.
  클러스터의 개수가 최적화되어 있으면 실루엣 계수의 값은 1에 가까운 값이 된다.
  실루엣 기법은 k-means 클러스터링 기법 이외에 다른 클러스터링에도 적용이 가능하다
'''
import numpy as np
from sklearn.metrics import silhouette_samples
from matplotlib import cm

# 데이터 X와 X를 임의의 클러스터 개수로 계산한 k-means 결과인 y_km을 인자로 받아 각 클러스터에 속하는 데이터의 실루엣 계수값을 수평 막대 그래프로 그려주는 함수를 작성함.
# y_km의 고유값을 멤버로 하는 numpy 배열을 cluster_labels에 저장. y_km의 고유값 개수는 클러스터의 개수와 동일함.

def plotSilhouette(x, pred):
    cluster_labels = np.unique(pred)
    n_clusters = cluster_labels.shape[0]   # 클러스터 개수를 n_clusters에 저장
    sil_val = silhouette_samples(x, pred, metric='euclidean')  # 실루엣 계수를 계산
    y_ax_lower, y_ax_upper = 0, 0
    yticks = []

    for i, c in enumerate(cluster_labels):
        # 각 클러스터에 속하는 데이터들에 대한 실루엣 값을 수평 막대 그래프로 그려주기
        c_sil_value = sil_val[pred == c]
        c_sil_value.sort()
        y_ax_upper += len(c_sil_value)

        plt.barh(range(y_ax_lower, y_ax_upper), c_sil_value, height=1.0, edgecolor='none')
        yticks.append((y_ax_lower + y_ax_upper) / 2)
        y_ax_lower += len(c_sil_value)

    sil_avg = np.mean(sil_val)         # 평균 저장

    plt.axvline(sil_avg, color='red', linestyle='--')  # 계산된 실루엣 계수의 평균값을 빨간 점선으로 표시
    plt.yticks(yticks, cluster_labels + 1)
    plt.ylabel('클러스터')
    plt.xlabel('실루엣 개수')
    plt.show() 

'''
그래프를 보면 클러스터 1~3 에 속하는 데이터들의 실루엣 계수가 0으로 된 값이 아무것도 없으며, 실루엣 계수의 평균이 0.7 보다 크므로 잘 분류된 결과라 볼 수 있다.
'''
X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)
km = KMeans(n_clusters=3, random_state=0) 
y_km = km.fit_predict(X)

plotSilhouette(X, y_km)