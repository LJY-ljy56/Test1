#使用bar（）绘制柱形图或堆积柱形图
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
#准备数据
x = np.arange(5)
y = np.array([9.7,9.6,9.5,9.5,9.4])
bar_width = 0.3
#绘制柱形图
plt.bar(x,y,tick_label=['肖申科的救赎','霸王别姬','阿甘正传','泰坦尼克号','这个杀手不太冷'], width=bar_width)
plt.show()