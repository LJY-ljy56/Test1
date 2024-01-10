#折线图
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
#准备数据
x =tick_label=['肖申科的救赎','霸王别姬','阿甘正传','泰坦尼克号','这个杀手不太冷']
y = np.array([9.7,9.6,9.5,9.5,9.4])
plt.xlabel('影片名')
plt.ylabel('评分')
#绘制图表
plt.plot(x,y)
#展示图表
plt.show()