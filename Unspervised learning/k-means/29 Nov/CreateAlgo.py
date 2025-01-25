import random

class MyOwnKmeansAlgo:
    def __init__(self, n_cluster = 2, max_iteration= 100):
        self.n_cluster = n_cluster
        self.max_iteration = max_iteration
        self.centroid = None

        def fit_predict(self,x):
            # print(x.shape)
            centers= random.sample(range(x.shape[0]),self.n_cluster)
            centroids = x[centers]

            return centroids
            