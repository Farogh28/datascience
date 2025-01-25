# from sklearn.datasets import make_blobs
# import matplotlib.pyplot as plt
# from CreateAlgo import MyOwnKmeansAlgo

# cluster_centroids = [(-5,5),(5,5)]
# cluster_std = (2,1)

# x,y = make_blobs(n_samples=100, centers= cluster_centroids, n_features= 2, random_state= 2)

# obj = MyOwnKmeansAlgo()
# centers= obj.fit_predict(x)

# print (centers[0][1])

# plt.scatter(x[:,0],x[:,1])
# plt.scatter(centers[0][0],centers[0][1],marker=".",s=50)
# plt.scatter(centers[1][0],centers[1][1],marker=".",s=50)

# plt.show()



# ----------------------------------------------

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from createalgonew import Ownkmeansalgo

cluster_centre = [(-5,5),(5,5)]
std=(2,2)

x,y =make_blobs(n_samples=100, centers= cluster_centre, n_features= 2, random_state= 2)

obj = Ownkmeansalgo()
centroids = obj.fit_predict(x)

plt.scatter(x[x:,0], x[:,1])
plt.scatter(centroids[0][0], centroids[0][1])
