import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from k_means import MyKmeansAlgo
df = pd.read_csv("data.csv")
my_predictor = MyKmeansAlgo()
new_dataset = df.drop(columns=["color"])

group_cluster,centroid,x = my_predictor.fit_predict(new_dataset)


# print(x)

plt.scatter(df["x"], df["y"])
plt.scatter(new_dataset[group_cluster == 0]["x"], new_dataset[group_cluster == 0]["y"])
plt.scatter(new_dataset[group_cluster == 1]["x"], new_dataset[group_cluster == 1]["y"])
plt.scatter(new_dataset[group_cluster == 2]["x"], new_dataset[group_cluster == 2]["y"])



# plt.scatter(centroid[0][0], centroid[0][1], s = 300)
# plt.scatter(centroid[1][0], centroid[1][1], s = 300)
# plt.scatter(centroid[2][0], centroid[2][1], s = 300)
# plt.show()


# plt.plot(range(1, max_k + 1), wcss, marker='o')
# plt.title('Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()

wcss = []
max_k = 10
for j in range(1, max_k + 1):
    kmeans = MyKmeansAlgo(n_cluster=j)
    kmeans.fit_predict(new_dataset)
    wcss.append(kmeans.calculate_wcss(new_dataset))

plt.figure(figsize=(10, 6))
plt.plot(range(1, max_k + 1), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# ---------------------------------------------------------



# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

# # Step 1: Prepare your dataset
# X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# # Step 2: Compute K-means for different values of k
# wcss = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(X)
#     wcss.append(kmeans.inertia_)

# # Step 3: Plot the WCSS against the number of clusters
# plt.plot(range(1, 11), wcss, marker='o')
# plt.title('Elbow Method')
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()
