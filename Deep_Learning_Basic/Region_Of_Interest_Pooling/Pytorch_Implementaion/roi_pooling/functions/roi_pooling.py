"""ROIPooling function and kernel

First version of CUDA kernel comes from:
-------------------------------------------------------------------------------
Fast R-CNN
Copyright (c) 2015 Microsoft
Licensed under The MIT License [see fast-rcnn/LICENSE for details]
Written by Ross Girshick
-------------------------------------------------------------------------------
"""
import torch
from torch.autograd import Function
from torch.autograd.function import once_differentiable
import torch.nn.functional as F
from ..utils import Dtype, Stream, load_kernel

CUDA_NUM_THREADS = 1024

# define kernel loop for short typing, as competition
kernel_loop = '''
    #define CUDA_KERNEL_LOOP(i,n) \
        for(int i = blockIdx.x * blockDim.x + threadIdx.x; \
        i < (n); \
        i += blockDim.x * gridDim.x)
'''

def GET_BLOCKS(N):
    return (N + CUDA_NUM_THREADS - 1)//CUDA_NUM_THREADS

_roipooling_kernel = kernel_loop + '''
extern "C"
__global__ void roi_pooling2d_forward_kernel

'''

