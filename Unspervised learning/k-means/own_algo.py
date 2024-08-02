import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from myKmeans_algo import MyKmeansAlgo

# generating data set via equation

from sklearn.datasets import make_blobs   # mainly a testing data set

cluster_centroid = [(-5 , 5), (5,5)]

cluster_std1 = [1 ,1]

# cluster_std1 = [2 ,1]   # ------- To spread dataset

x ,y = make_blobs (n_samples= 100, centers= cluster_centroid, cluster_std= cluster_std1, 
                   n_features= 2, random_state= 2)


kmeans = MyKmeansAlgo()

cluster_group, centroid =kmeans.fit_predict(x)
print (centroid)
# only x contains the dataset and y contains the values

# print (x.shape)
# print (x,y)

plt.scatter (x[cluster_group == 0,0], x[cluster_group == 0 ,1], color = "red", label = "0th cluster")
plt.scatter (x[cluster_group == 1,0], x[cluster_group == 1,1], color = "green", label = "1st cluster")
plt.scatter (centroid[0][0], centroid [0][1], color = "black", label = "1st Centroids")
plt.scatter (centroid[1][0], centroid [1][1], color = "black", label = "2nd Centroids")
plt.show()
plt.legend()

# print (cluster_centroid)

