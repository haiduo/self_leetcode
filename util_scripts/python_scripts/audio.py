import torch
import torchaudio
import matplotlib.pyplot as plt
# from soundfile import SoundFile

# import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE" #https://zhuanlan.zhihu.com/p/371649016
# myfile = SoundFile("kalong.wav")
# sound =AudioSegment.from_file("kalong.mp3", format = 'MP3') #https://blog.csdn.net/qq_38161040/article/details/91832980
# device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
waveform, sample_rate = torchaudio.load("kalong.wav")
print(waveform.shape, sample_rate)

plt.plot(waveform[:,0:sample_rate*17].t().numpy()) #t()为转置操作 numpy()为转numpy


plt.show()
