import matplotlib.pyplot as plt
import numpy as np

x=[1,1,4,5,1,4]
y=[1,9,1,9,8,1]
c=[0,20,30,40,50,60]
plt.scatter(x,y,c=c,cmap='viridis') 
#颜色图有多种种类
plt.colorbar()
#包含颜色图
plt.show()
