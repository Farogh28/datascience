# 1) Decide n_cluster
# 2) initialize Cluster
# 3) Assign Cluster 
# 4) move cluster
# 5) Finish

# initializing centroid
import random
import numpy as np

class MyKmeansAlgo:
    def __init__(self, n_cluster = 2, max_iteration = 100): 
        self.n_cluster = n_cluster
        self.max_iteration = max_iteration
        self.centroids = None

    def fit_predict (self, x ):
        # print (x.shape)
        # random.sample(range, (length)how many points to choose)
        random_index = random.sample(range(x.shape[0]), self.n_cluster)

        self.centroids = x[random_index]   # to get specific data or index 

        # return self.centroids
    # 3) Assign Cluster 
    
        cluster_group = self.assign_cluster(x)   # create a function assign_cluster and pass parameter centroid and x / passed as self coz its inside a class

        return cluster_group, self.centroids
    def assign_cluster(self, x):
        distance = []
        cluster_group = []

        for i in x:
            for centroid in self.centroids:
                distance.append(np.sqrt(np.dot(i - centroid, i - centroid)))
            # print(distance)
            # distance.clear()
            min_distance = min (distance)
            cluster_group.append(distance.index(min_distance))   # To get min value of distance
            distance.clear()
        return np.array(cluster_group)