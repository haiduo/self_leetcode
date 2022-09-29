import torch
a = torch.tensor([1,2,3.], requires_grad = True)
out = a.sigmoid()
c = out.data  # 需要注意的是，通过.data “分离”得到的的变量会和原来的变量共用同样的数据，
              # 而且新分离得到的张量是不可求导的，c发生了变化，原来的张量也会发生变化
c.zero_()     # 改变c的值，原来的out也会改变
print(c.requires_grad)
print(c)
print(out.requires_grad)
print(out)
print("----------------------------------------------")
out.sum().backward() # 对原来的out求导，
print(a.grad)  # 不会报错，但是结果却并不正确
'''运行结果为：
False
tensor([0., 0., 0.])
True
tensor([0., 0., 0.], grad_fn=<SigmoidBackward>)
----------------------------------------------
tensor([0., 0., 0.])
'''

