import torch
from torch import nn


x = torch.rand(10, 20, 5, 5)*10000
# 分成 4 个 group
gn = nn.GroupNorm(num_groups=4, num_channels=20, eps=0, affine=False)
official_gn = gn(x)

#把同一个group的元素融合到一起
# 分成 4 个 group

x1 = x.view(10, 4, -1)
print("x1.mean:",x1.mean(dim=-1).shape)
mu = x1.mean(dim=-1).reshape(10, 4, -1)
std = x1.std(dim=-1).reshape(10, 4, -1)

x1_norm = (x1 - mu)/std
print(x1_norm.shape)
my_gn = x1_norm.reshape(10, 20, 5, 5)

diff = (my_gn - official_gn).sum()

print('diff={}'.format(diff))