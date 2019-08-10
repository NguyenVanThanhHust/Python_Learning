from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

plt.figure('Iris dataset', figsize=(7,5))
ax = plt.axes(projection = '3d')
ax.scatter(X_iris[:,3],X_iris[:,0],X_iris[:,1],c=y_iris);

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# color missclassified data
centroids = k_means.cluster_centers_
ax.scatter(X_iris[k_means_predicted!=y_iris,3],X_iris[k_means_predicted!=y_iris,0],X_iris[k_means_predicted!=y_iris,2] ,
           c='b', s=50)

# plot centroids

ax.scatter(centroids[0,3],centroids[0,0],centroids[0,2] ,c='r', s=50, label='centroid')
ax.scatter(centroids[1,3],centroids[1,0],centroids[1,2] ,c='r', s=50)
ax.scatter(centroids[2,3],centroids[2,0],centroids[2,2] ,c='r', s=50)