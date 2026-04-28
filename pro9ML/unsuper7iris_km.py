# kmeans : iris dataset - 군집분석, 정량평가, 클러스터별 평균비교(ANOVA)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score

# adjusted_rand_score : 군집 vs 실제 라벨 비교
# normalized_mutual_info_score : 정보량 기반 유사도(같은 정보 공유)
# silhouette_score : 군집 자체 품질 평가(군집에 잘 속해있는가 확인)

from sklearn.decomposition import PCA # 4차원 -> 2차원으로 압축
iris = load_iris()
x = iris.data
y = iris.target
feature_names = iris.feature_names

df = pd.DataFrame(x, columns=feature_names)
print(df.head(3), df.shape)

# Scaling
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled[:2])
# [[-0.90068117  1.01900435 -1.34022653 -1.3154443 ]
#  [-1.14301691 -0.13197948 -1.34022653 -1.3154443 ]]

# kmeans 모델
k = 3
kmeans = KMeans(
    n_clusters=k,
    init='k-means++',
    n_init=10,      # k-means 10번 수행, 가장 오차(inertia)가 작은 결과를 선택
    random_state=42
)

clusters = kmeans.fit_predict(x_scaled)
df['cluster'] = clusters
print('cluster 중심값 : ', kmeans.cluster_centers_)
# [[-0.05021989 -0.88337647  0.34773781  0.2815273 ]
#  [-1.01457897  0.85326268 -1.30498732 -1.25489349]
#  [ 1.13597027  0.08842168  0.99615451  1.01752612]]

# PCA (시각화용)
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scaled)
print(x_pca[:2])
# [[-2.26470281  0.4800266 ]
#  [-2.08096115 -0.67413356]]
print('pca 설명 분산 비율 : ', pca.explained_variance_ratio_) # [0.72962445 0.22850762] --> 95%

# 시각화 - pca기반, 4개의 열을 2차원 차트에 표현 불가능하기 때문
plt.figure(figsize=(6, 5))
sns.scatterplot(x = x_pca[:, 0], y = x_pca[:, 1], hue=clusters, palette='Set1')
plt.title('K-Means Iris clustering')
plt.xlabel('pc1(제 1주성분)')
plt.ylabel('pc2(제 2주성분)')
plt.show()

# 실제 라벨과 군집 비교(교차표)
ct = pd.crosstab(y, clusters)
print(ct)
# col_0   0   1   2 <-- 군집 id(0 - cluster1, 1 - cluster2, 2 - cluster3)
# row_0            
# 0       0  50   0
# 1      39   0  11
# 2      14   0  36
# 행 : 실제 label(0 - setosa, 1 - versicolor, 2 - virginica)

print('class별 대표 군집')
for i in range(ct.shape[0]):
    max_cluster = ct.iloc[i].idxmax()
    print(f'실제 class {i} -> 군집 {max_cluster}, 갯수 : {ct.iloc[i].max()}')

print('------ 정량 평가 ------')
ari = adjusted_rand_score(y, clusters)
nmi = normalized_mutual_info_score(y, clusters)
sil_score = silhouette_score(x_scaled, clusters)

print('ARI : ', ari) # ARI(군집 vs 실제 라벨 비교) :  0.6201351808870379
print('NMI : ', nmi) # NMI(정보량 기반 유사도) :  0.659486892724918
print('silhouette_score : ', sil_score) 
# silhouette_score(군집 자체 품질 평가) :  0.45994823920518635 (1에 가까울수록 좋은거)
# 군집 내 요소끼리는 거리가 가깝고, 다른 군집과는 거리가 먼게 좋은 군집의 특징임.

# k=3을 사용했는데 3이 합리적인지 확인하기 : 엘보우 기법
inertia_list = []
k_range = range(1, 10)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(x_scaled)
    inertia_list.append(km.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(k_range, inertia_list, marker='o')
plt.title('엘보우 기법')
plt.xlabel('클러스터 수(k)')
plt.ylabel('inertia')
plt.show() #k가 3인 경우가 가장 적당함.


# 실제 vs 군집 비교 시각화
plt.figure(figsize=(12, 5))
# 실제 라벨
plt.subplot(1, 2, 1)
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=y, palette='Set1')
plt.title('실제 라벨')

# 군집 결과
plt.subplot(1, 2, 2)
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=clusters, palette='Set1')
plt.title('군집 결과')
plt.show()

# 클러스터별 평균 분석
cluster_mean = df.groupby('cluster').mean()
print('클러스터별 평균 : ', cluster_mean)
# 클러스터별 평균 :           sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# cluster                                                                          
# 0                 5.801887          2.673585           4.369811          1.413208
# 1                 5.006000          3.428000           1.462000          0.246000
# 2                 6.780851          3.095745           5.510638          1.972340

# 군집 3개 : 군집 간 평균차이 검정(ANOVA)
# 귀무가설 : 군집간 평균의 차이가 없다.
# 대립가설 : 군집간 평균의 차이가 있다.

# ANOVA
from scipy.stats import f_oneway

for col in feature_names:   #각 군집별 데이터 분리
    group0 = df[df['cluster'] == 0][col]
    group1 = df[df['cluster'] == 1][col]
    group2 = df[df['cluster'] == 2][col]

    # ANOVA 수행
    f_stat, p_value = f_oneway(group0, group1, group2)
    print(f'{col} : f-statistic : {f_stat:.4f}, p-value : {p_value}')

    # 해석
    if p_value >= 0.05:
        print('군집간 평균에 차이가 없다.(귀무가설 채택)')
    else:
        print('군집간 평균에 차이가 있다.(대립가설 채택)')

# K-Means가 꽃받침, 꽃잎 길이/너비를 제대로 군집분석했음을 알 수 있다.

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# petal length로 작업
feature = 'petal length (cm)'
tukey = pairwise_tukeyhsd(
    endog=df[feature], groups=df['cluster'], alpha=0.05
)
print('tukeyhsd 결과(petal length) : ', tukey)
# ===================================================
# group1 group2 meandiff p-adj  lower   upper  reject
# ---------------------------------------------------
#      0      1  -2.9078   0.0 -3.1405 -2.6751   True
#      0      2   1.1408   0.0  0.9043  1.3773   True
#      1      2   4.0486   0.0  3.8088  4.2884   True
# ---------------------------------------------------

# 사후 검정 시각화
tukey.plot_simultaneous(figsize=(6, 4))
plt.title(f'tukeyhsd - {feature}')
plt.xlabel('평균 차이')
plt.show()

# 그래프에서 점은 평균값을, 가로 선은 신뢰구간을 나타냅니다.

# 선이 겹치지 않는다: 세 군집의 가로 선이 서로 전혀 겹치지 않고 멀리 떨어져 있죠? 이건 **"이 군집들은 꽃잎 길이로 봤을 때 완전히 독립적인 세 집단이다"**라는 것을 시각적으로 증명하는 겁니다.

# 군집의 특징 파악:

# 가장 왼쪽 (1번 군집): 꽃잎 길이가 가장 짧은 집단입니다. (Setosa일 확률이 매우 높음)

# 가운데 (0번 군집): 중간 정도의 길이를 가진 집단입니다.

# 가장 오른쪽 (2번 군집): 꽃잎 길이가 가장 긴 집단입니다.

# 군집별 boxplot
for col in feature_names:
    plt.figure(figsize=(5, 3))
    sns.boxplot(x = 'cluster', y = col, data=df)
    plt.title(f'{col} by cluster')
    plt.show()

print()
# cluster 평균분석 마지막 열에 Type 추가
cluster_mean['label'] = ['Type A', 'Type B', 'Type C']
print(cluster_mean)