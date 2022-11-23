import itertools
import time
import numpy as np

def convolve2d(arr, kernel, stride=1, padding='same'):
    '''
    Using convolution kernel to smooth image

    Parameters
    ===========
    arr: 3D array or 3-channel image
    kernel: Filter matrix
    stride: Stride of scanning
    padding: padding mode
    '''
    h, w, channel = arr.shape
    k = kernel.shape[0]
    r = int(k/2)
    kernel_r = np.rot90(kernel, k=2, axes=(0,1))   #将矩阵旋转180度 狭义卷积操作，一般深度学习不用这样
    # padding outer area with 0
    padding_arr = np.zeros([h+k-1, w+k-1, channel])
    padding_arr[r:h+r, r:w+r] = arr 
    new_arr = np.zeros(arr.shape)
    for i in range(r, h+r, stride):
        for j in range(r, w+r, stride): 
            roi = padding_arr[i-r:i+r+1,j-r:j+r+1]
            new_arr[i-r,j-r] = np.sum(np.sum(roi*kernel_r,axis=0),axis=0)
    return new_arr[::stride,::stride]

# 方法2 向量化索引运算
def convolve2d_vector(arr, kernel, stride=1, padding='same'):
    h, w, channel = arr.shape[0],arr.shape[1],arr.shape[2]
    k = kernel.shape[0]
    r = int(k/2)
    kernel_r = np.rot90(kernel,k=2,axes=(0,1))
    # padding outer area with 0
    padding_arr = np.zeros([h+k-1,w+k-1,channel])
    padding_arr[r:h+r,r:w+r] = arr 
    new_arr = np.zeros(arr.shape)

    vector = np.array(list(itertools.product(np.arange(r,h+r,stride),np.arange(r,w+r,stride))))
    vi = vector[:,0]
    vj = vector[:,1]  
    def _convolution(vi,vj):
        roi = padding_arr[vi-r:vi+r+1,vj-r:vj+r+1]
        new_arr[vi-r,vj-r] = np.sum(np.sum(roi*kernel_r,axis=0),axis=0)
    vfunc = np.vectorize(_convolution)    # 把函数向量化 本质还是一个for loop，没起到多大作用
    vfunc(vi,vj)
    return new_arr[::stride,::stride]

# 方法3 img2clo
def convolve2d_img2clo(arr, kernel, stride=1, padding='same'):
    h, w, channel = arr.shape[0],arr.shape[1],arr.shape[2]
    k, n = kernel.shape[0], kernel.shape[2]
    r = int(k/2)
    #重新排列kernel为左乘矩阵，通道channel前置以便利用高维数组的矩阵乘法
    matrix_l = kernel.reshape((1,k*k,n)).transpose((2,0,1))
    padding_arr = np.zeros([h+k-1,w+k-1,channel])
    padding_arr[r:h+r,r:w+r] = arr
    #重新排列image为右乘矩阵，通道channel前置
    matrix_r = np.zeros((channel,k*k,h*w))
    for i in range(r,h+r,stride):
        for j in range(r,w+r,stride): 
            roi = padding_arr[i-r:i+r+1,j-r:j+r+1].reshape((k*k,1,channel)).transpose((2,0,1))
            matrix_r[:,:,(i-r)*w+j-r:(i-r)*w+j-r+1] = roi[:,::-1,:]        
    result = np.matmul(matrix_l, matrix_r)  #空间换时间
    out = result.reshape((channel,h,w)).transpose((1,2,0))
    return out[::stride,::stride]

if __name__=='__main__':
    A = np.arange(1,10001).reshape((100,100,1))
    print(A.shape)
    kernel = np.arange(1,10).reshape((3,3,1))/45
    # convert to 3-channels
    A3 = np.concatenate((A, 2*A, 3*A), axis=-1)
    k3 = np.concatenate((kernel, kernel, kernel), axis=-1)

    t1 = time.time()
    for i in range(100):
        B1 = convolve2d(A3, k3, stride=2).astype(int)
    t2 = time.time()
    print(t2-t1)

    t1 = time.time()
    for i in range(100):
        B2 = convolve2d_vector(A3, k3, stride=2).astype(int)
    t2 = time.time()
    print(t2-t1)

    t1 = time.time()
    for i in range(100):
        B3 = convolve2d_img2clo(A3, k3, stride=2).astype(int)
    t2 = time.time()
    print(t2-t1)

    print(B1.all()==B2.all()==B2.all())
