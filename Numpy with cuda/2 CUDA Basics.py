import numpy as np
import math
import scipy.stats
import time

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
b_col = b[:, np.newaxis]
c = np.arange(4*4).reshape((4,4))

# c = np.add(a, b)
# print("np.add(a, b) = ", c)
# d = np.add(a, 100)
# print("np.add(a, 100) = ", d)

# c = np.arange(4*4).reshape((4,4))
# print('c:', c)

# d = np.add(b, c)
# print('d: ', d)

# e = np.add(b_col, c)
# print("e: ", e) 

#Making ufuncs for the GPU

# Note : default type in numpy array is int32, if you want to use int64, declare it
from numba import vectorize
@vectorize(['int32(int32, int32)'], target = 'cuda')
def add_ufunc(x, y):
    return x + y
    
print('a+b:\n', add_ufunc(a, b))
print()
print('b_col + c:\n', add_ufunc(b_col, c))

"""
# int64 version
a = np.array([1, 2, 3, 4], dtype = 'int64')
b = np.array([10, 20, 30, 40], dtype = 'int64')
b_col = b[:, np.newaxis]
c = np.arange(4*4).reshape((4,4), dtype = 'int64')
from numba import vectorize
@vectorize(['int64(int64, int64)'], target = 'cuda')
def add_ufunc(x, y):
    return x + y
    
print('a+b:\n', add_ufunc(a, b))
print()
print('b_col + c:\n', add_ufunc(b_col, c))
"""



sqrt_2PI = np.float32((2 * math.pi) ** 0.5)

@vectorize(['float32(float32, float32, float32)'], target = 'cuda')
def gaussian_pdf(x, mean, sigma):
    """
    Compute the value of a Gaussian probability density function
    """
    return math.exp( -0.5* ((x - mean)/ sigma)**2) / (sigma * sqrt_2PI)
    
# Evaluate the Gaussian a million times!
x = np.random.uniform(-2, 3, size = 1000000).astype(np.float32)
mean = np.float32(0.0)
sigma = np.float32(1.0)

norm_pdf = scipy.stats.norm

start = time.time()
norm_pdf.pdf(x, loc=mean, scale=sigma)
end = time.time()
print("Take: ", (end - start) *10)

start_2 = time.time()
gaussian_pdf(x, mean, sigma)
end_2 = time.time()
print("Take: ", (end_2 - start_2) *10)

from numba import cuda

@cuda.jit(device=True)
def polar_to_cartesian(rho, theta):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y  # This is Python, so let's return a tuple

@vectorize(['float32(float32, float32, float32, float32)'], target='cuda')
def polar_distance(rho1, theta1, rho2, theta2):
    x1, y1 = polar_to_cartesian(rho1, theta1)
    x2, y2 = polar_to_cartesian(rho2, theta2)
    
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
n = 1000000
rho1 = np.random.uniform(0.5, 1.5, size=n).astype(np.float32)
theta1 = np.random.uniform(-np.pi, np.pi, size=n).astype(np.float32)
rho2 = np.random.uniform(0.5, 1.5, size=n).astype(np.float32)
theta2 = np.random.uniform(-np.pi, np.pi, size=n).astype(np.float32)
print(polar_distance(rho1, theta1, rho2, theta2))