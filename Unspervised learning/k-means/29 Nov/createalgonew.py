# 1) Decide n_cluster
# 2) initialize centroid
# 3) assign
# 4)move centroid
# 5) Finish





import numpy as np
class Ownkmeansalgo:   
    def __init__(self, n_cluster = 2, max_itteration = 100):
        self.n_cluster = n_cluster
        self.max_itteration =max_itteration
        self.centroid = None
    
    def fit_predict(self, dataset):
        print(dataset.shape)
        # 2) Initialize centroid
        # print (dataset)

        self.centroid = random.sample(range(dataset.shape[0]),self.n_cluster)  # random point ko centroid bna rhe

        self.centroid= dataset[centroid]   #dataset me se given location find krne ka

        # print(self.centroid)

# 3) Assign cluster

        self.calculate_distance(dataset)   #centroid pass nahi kr rhe bcoz attribute he

        return self.centroid
    def calculate_distance(self, dataset):
        # pass
    # np.sqrt(np.dot(b-a,b-a))
        distance= []

        cluster_group = []
        for row in dataset:  # to get the data from the dataset to calculate the ditance.
            print(row,"roww is here")
            for centroid in self.centroid:
                print (centroid)
                distance.append( np.sqrt(np.dot(row- centroid, row- centroid)))
            print(distance, "distance")
            print(min(distance),"minimum")  # to get the minimum value from all distance 
            
            cluster_group.append(distance.index(min(distance))) #cluster grp ke insdie append kr rhe he distance ke idex ka min wala distance
            distance.clear()
        return np.array(cluster_group)  # to get the cluster_group values in array format
    


    # 4) MOVE CENTROID

    def move_centroid(dataset, cluster):
         
         new_centroids = []
         clusterss = np.unique(cluster)
         for i in clusterss:
            new_centroids.append(dataset[cluster ==i].mean(axis = 0))    
        # print(cluster)
            # print(dataset[cluster==0].mean(axis = 0))   # .mean is to calculate the mean//  and axis
            return np.array(new_centroids)



# 5) finish 