# -*- coding:utf-8 -*-
import torch
import torch.nn as nn
import torchvision

#使用了YOLOPNet网络
model = get_net(cfg)
checkpoint = torch.load(r'C:\Users\haidu\Desktop\temp\python_scripts\model_best.pth', map_location= torch.device('cuda:0'))
model = model.load_state_dict(checkpoint)

#加载权重参数到device上
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
#加载权重参数到device上
model.eval()

BATCH_SIZE=32
#伪造一个输入
dummy_input = torch.randn(BATCH_SIZE, 3, 224, 224).to(device)

#定义网络输入输出的名字
input_names = ['YoloP_int']
output_names = ['YoloP_out']
#使用pytorch的onnx模块来进行转换
torch.onnx.export(model,
                  dummy_input,
                  "YoloP.onnx",
                  verbose=False,
                  input_names=input_names,
                  output_names=output_names)