# coding;utf8
import torch
from torch import nn

x = torch.randn(10, 3, 5, 5)*10000 #x.shape:[10,3,5,5]

# normalization_shape 相当于告诉程序这本书有多少页，每页多少行多少列
# eps=0 排除干扰
# elementwise_affine=False 不作映射
# 这里的映射和 BN 以及下文的 IN 有区别，它是 elementwise 的 affine，
# 即 gamma 和 beta 不是 channel 维的向量，而是维度等于 normalized_shape 的矩阵
ln = nn.LayerNorm(normalized_shape=[3,5,5], eps=0, elementwise_affine = False)

official_ln = ln(x)

# 把 channel 维度单独提出来，而把其它需要求均值和标准差的维度融合到一起
x1 = x.contiguous().view(10, -1)

# x1.mean(dim=1).shape: [10]
print("x1.mean:",x1.mean(dim=1).shape)
mu = x1.mean(dim=1).view(10, 1, 1, 1)

# unbiased=False, 求方差时不做无偏估计（除以 N-1 而不是 N），和原始论文一致 unbiased = False
# x1.std(dim=1).shape: [3]

std = x1.std(dim=1, unbiased=False).view(10, 1, 1, 1)
my_ln = (x - mu)/std


diff = (official_ln - my_ln).sum()

print('diff={}'.format(diff))