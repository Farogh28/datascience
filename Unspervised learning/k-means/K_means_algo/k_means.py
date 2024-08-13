import random
import numpy as np


class MyKmeansAlgo:
    def __init__(self, n_cluster=3, max_itteration=100):
        self.n_cluster = n_cluster
        self.max_itteration = max_itteration
        self.centroid = None

    def fit_predict(self, dataset):
        centroid_index = random.sample(range(dataset.shape[0]), self.n_cluster)
        dataset = dataset.values
        # print(type(dataset))
        self.centroid = dataset[centroid_index]

        x = 0
        for i in range(self.max_itteration):
            x += 1

            # 3) Assign Cluster
            group_cluster = self.assign_cluster(dataset)

            # 4) Move Centroid
            new_centroids = self.move_centroid(dataset, group_cluster)
            old_centroids = self.centroid
            self.centroid = new_centroids

            # 5) Finish
            if (old_centroids == self.centroid).all():
                break

        return group_cluster, self.centroid, x

    def assign_cluster(self, dataset):
        cluster_group = []
        distance = []
        for i in dataset:
            for centroid in self.centroid:
                distance.append(np.sqrt(np.dot(i - centroid, i - centroid)))
            # print(distance)
            min_distance = min(distance)
            cluster_group.append(distance.index(min_distance))
            distance.clear()
        return np.array(cluster_group)

    def move_centroid(self, dataset, group_cluster):
        new_centroid = []
        cluster_type = np.unique(group_cluster)

        for type in cluster_type:
            new_centroid.append(dataset[group_cluster == type].mean(axis=0))

        return np.array(new_centroid)


# -------------------------------------------------------

# def calculate_wcss(self, dataset, group_cluster):
#         wcss = 0
#         for i, centroid in enumerate(self.centroid):
#             cluster_points = dataset[group_cluster == i]
#             wcss += np.sum((cluster_points - centroid) ** 2)
#         return wcss

# def apply_elbow_method(dataset, max_k=10):
#     wcss = []
#     for k in range(1, max_k + 1):
#         kmeans = MyKmeansAlgo(n_cluster=k)
#         group_cluster, _ = kmeans.fit_predict(dataset)
#         wcss.append(kmeans.calculate_wcss(dataset.values, group_cluster))


# -------------------------------------------------------------

    def calculate_wcss(self, dataset):
        dataset = dataset.values
        group_cluster = self.assign_cluster(dataset)
        # print(group_cluster)
        wcss = 0

        for i, cluster in enumerate(group_cluster):
            wcss += np.sum((dataset[i] - self.centroid[cluster]) ** 2)

        return wcss
