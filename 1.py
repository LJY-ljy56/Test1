#条形图
#使用barh()绘制堆积条形图
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
#准备数据
y = np.arange(5)
x = np.array([9.7,9.6,9.5,9.5,9.4])
bar_height = 0.3
plt.xlabel('评分')
plt.ylabel('影片名')
#绘制图表
plt.barh(y,x,tick_label=['肖申科的救赎','霸王别姬','阿甘正传','泰坦尼克号','这个杀手不太冷'],height=bar_height)
#展示图表
plt.show()