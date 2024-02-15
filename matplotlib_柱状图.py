import matplotlib.pyplot as plt
import numpy as np

x=['A','B','C','D','E','F']
y=[1,9,1,9,8,1]
c=['red','red','blue','blue','pink','pink']
plt.subplot(1,2,1)#1行2张第1个
plt.bar(x,y,color='red',width=0.2)#纵向图
#width设定每个柱子宽度
plt.subplot(1,2,2)#1行2张第2个
plt.barh(x,y,height=0.3)#横向图
#height设定每个柱子高度



plt.show()
