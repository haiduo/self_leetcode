# -*- coding:utf-8 -*-
import torch
import torch.nn as nn
import torchvision
#使用了MobileNet网络
model = torchvision.models.mobilenet_v2(pretrained=True)
# torchvision的models中没有softmax层，我们添加一个
model = nn.Sequential(model, nn.Softmax(dim=1))
#加载权重参数到device上
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
#加载权重参数到device上
model.to(device)
model.eval()
#伪造一个输入
dummy_input = torch.randn(1, 3, 224, 224).to(device)
# dummy_input = torch.randn(1, 3, 224, 224)
#定义网络输入输出的名字
input_names = ['image']
output_names = ['gemfield_out']
#使用pytorch的onnx模块来进行转换
torch.onnx.export(model,
                  dummy_input,
                  "mobilenet_v2.onnx",
                  verbose=False,
                  input_names=input_names,
                  output_names=output_names)