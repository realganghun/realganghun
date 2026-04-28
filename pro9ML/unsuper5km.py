import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
from sklearn.cluster import KMeans

students = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
scores = np.array([76, 95, 65, 85, 60, 92, 55, 88, 83, 72]).reshape(-1, 1) # 열 하나 행은 알아서 판단하는걸로....
print('점수 : ', scores)

# k = 3
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)
km_clusters = kmeans.fit_predict(scores)
print(km_clusters)

df = pd.DataFrame({
    'student':students,
    'score':scores.ravel(),
    'cluster':km_clusters
})
print(df)

print('\n 군집별 평균 점수')
grouped = df.groupby('cluster')['score'].mean()
print(grouped)

# 시각화
x_position = np.arange(len(students))
y_scores = scores.ravel()
colors = {0:'red', 1:'blue', 2:'green'}
plt.figure(figsize=(10, 6))

for i, (x, y, cluster) in enumerate(zip(x_position, y_scores, km_clusters)):
    plt.scatter(x, y, color=colors[cluster], s=100)
    plt.text(x, y + 1.5, students[i], fontsize=10, ha='center')

# 중심점
centers = kmeans.cluster_centers_
for center in centers:
    plt.scatter(len(students) // 2, center[0], marker='X', c='black', s=200)
    
plt.xticks(x_position, students)
plt.xlabel('학생명')
plt.ylabel('점수')
plt.grid(True)
plt.show()