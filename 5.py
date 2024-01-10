#饼图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#准备数据
kinds = ['肖申科的救赎','霸王别姬','阿甘正传','泰坦尼克号','这个杀手不太冷']
money_scale= [9.7,9.6,9.5,9.5,9.4]
dev_position = [0.1,0.1,0.1,0.1,0.1]
#绘制饼图
plt.pie(money_scale,labels=kinds,autopct='%3.1f%%',shadow=True,explode=dev_position,startangle=90)
#展示图表
plt.show()