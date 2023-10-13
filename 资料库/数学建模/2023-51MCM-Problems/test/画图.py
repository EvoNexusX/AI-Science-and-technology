#导入需要用到的库
import math

import numpy as np
import matplotlib.pyplot as plt
import math
#设置x坐标轴的起始点为0、终点为10，中间有1000个点
x = np.linspace(0,10,1000)
m=50
g=10
k=0.02
y = math.sqrt(m*g/k)*(pow(math.e,2*math.sqrt(g*k/m)*x-1))/(pow(math.e,2*math.sqrt(g*k/m)*x+1))
print(y)
#定义一个图像窗口
plt.figure()
#绘制曲线,参数依次代表要画的两个变量、公式图线颜色、公式图线宽度、公式图线以不连续线组成、
plt.plot(x,y,color = "blue",linewidth = 1,linestyle = "--")

#设置横轴标签
plt.xlabel("X")
#设置纵轴标签
plt.ylabel("Y")
#设置横轴精准刻度
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
# #设置纵轴精准刻度
plt.yticks(21.)
#呈现图像
plt.show()

