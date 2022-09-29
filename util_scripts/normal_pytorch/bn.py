# coding;utf8
import torch
from torch import nn

# track_running_stats=False，求当前 batch 真实平均值和标准差，
# s
# affine=False, 只做归一化，不乘以 gamma 加 beta（通过训练才能确定）
# num_features 为 feature map 的 channel 数目
# eps 设为 0，让官方代码和我们自己的代码结果尽量接近

bn = nn.BatchNorm2d(num_features=3, eps=0, affine=False, track_running_stats=False)

x = torch.randn(10, 3, 5, 5)*10000 #x.shape:[10,3,5,5]
official_bn = bn(x)

# 把 channel 维度单独提出来，而把其它需要求均值和标准差的维度融合到一起

# x.permute(1, 0, 2, 3).shape: [c,n,h,w]
# x.permute(1, 0, 2, 3).contiguous(): [c,n,h,w]
# x.permute(1, 0, 2, 3).contiguous().view(3, -1): [c, n x h x w]

# x1 = x.permute(1, 0, 2, 3).contiguous().view(3, -1)
x1 = x.transpose(0,1).contiguous().view(3,-1)

# x1.mean(dim=1).shape: [3]
print("x1.mean:",x1.mean(dim=1))
mu = x1.mean(dim=1).view(1, 3, 1, 1)

# unbiased=False, 求方差时不做无偏估计（除以 N-1 而不是 N），和原始论文一致 unbiased = False
# x1.std(dim=1).shape: [3]
std = x1.std(dim=1, unbiased=False).view(1, 3, 1, 1)
my_bn = (x - mu)/std

diff = (official_bn - my_bn).sum()
print(my_bn.shape)

print('diff={}'.format(diff))