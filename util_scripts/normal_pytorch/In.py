import torch
from torch import nn


x = torch.rand(10, 3, 5, 5) * 10000

# track_running_stats=False，求当前 batch 真实平均值和标准差，
# 而不是更新全局平均值和标准差
# affine=False, 只做归一化，不乘以 gamma 加 beta（通过训练才能确定）
# num_features 为 feature map 的 channel 数目
# eps 设为 0，让官方代码和我们自己的代码结果尽量接近

In = nn.InstanceNorm2d(num_features=3, eps=0, affine=False, track_running_stats=False)

offcial_in = In(x)

x1 = x.view(30, -1)
print("x1.mean:",x1.mean(dim=1).shape)
mu = x1.mean(dim=1).view(10, 3, 1, 1)
std = x1.std(dim=1, unbiased=False).view(10, 3, 1, 1)

my_in = (x - mu)/std

diff = (my_in - offcial_in).sum()
print('diff={}'.format(diff))