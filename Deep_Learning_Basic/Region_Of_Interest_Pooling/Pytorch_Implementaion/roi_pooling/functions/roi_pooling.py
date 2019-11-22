"""ROIPooling function and kernel

Modified work:
-------------------------------------------------------------------------------
Copyright (c) 2019 Victor Escorcia
-------------------------------------------------------------------------------

Original from work of _roipooling_kernel and
_roipooling_kernel_backward_grad_input:
-------------------------------------------------------------------------------
Copyright (c) 2015 Preferred Infrastructure, Inc.
Copyright (c) 2015 Preferred Networks, Inc.
Licensed under The MIT License [see chainer/LICENSE for details]
-------------------------------------------------------------------------------

First version of CUDA kernel comes from:
-------------------------------------------------------------------------------
Fast R-CNN
Copyright (c) 2015 Microsoft
Licensed under The MIT License [see fast-rcnn/LICENSE for details]
Written by Ross Girshick
-------------------------------------------------------------------------------
"""

import torch
import torch.autograd import Function
from torch.autograd.function import once_differentiable
import torch.nn.functional as F
from ..utils import Dtype, Stream, load_kernel

CUDA_NUM_THREADS = 1024
kernel_loop = '''
#define CUDA_KERNEL_LOOP(i, n) \
    for (int i = blockIdx.x * blockDim.x + threadIdx.x; \
        i < (n) ;\
        i += blockDim.x * gridDim.x)
'''

def GET_BLOCK(N):
    return (N + CUDA_NUM_THREADS - 1) // CUDA_NUM_THREADS

# following function will loop through feature map
# assign each position in feature map a thread
# 
# Input :
# const ${Dtype}* bottom_data array of feature map type: float/double/int 
# const ${Dtype}* bottom_rois array of output 
_roipooling_kernel = kernel_loop + '''
extern "C"
__global__ void roi_pooling2d_forwardKernel(const ${Dtype}* bottom_data, const ${Dtype}* bottom_rois,
    ${Dtype}* top_data, ${Dtype_ind}* argmax_data))
{
    CUDA_KERNEL_LOOP(index, ${nthreads})
    {
        // position in output filter
        int pw = index % ${pooled_width};
        int ph = (index / ${pooled_width}) % ${pooled_height};
        int c = ((index / ${pooled_width} ) / ${pooled_height}) % ${channels};
        int num = index / ${pooled_width} / ${pooled_height}/ ${channels};

        int roi_batch_ind = bottom_rois[num * 5 + 0];
        int roi_start_w = round(bottom_rois[num * 5 + 1] * ${spatial_scale});
        int roi_start_h = round(bottom_rois[num * 5 + 2] * ${spatial_scale});
        int roi_end_w = round(bottom_rois[num * 5 + 3] * ${spatial_scale});
        int roi_end_h = round(bottom_rois[num * 5 + 4] * ${spatial_scale});   

        // Force malformed ROIs to be 1x1
    }
}
'''


