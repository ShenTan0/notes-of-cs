import matplotlib.pyplot as plt
import numpy as np
x=range(6)
y=[1,9,1,9,8,1]

# plt.plot(x,y)  #仅以线绘制,每条线连接两个点
# plt.plot(x,y,'o') #绘图without line


#标记 
plt.plot(x,y,marker='o',ms=10,mec='red',mfc='red',
         linestyle='--',color='purple',linewidth=2.5)
# 点(marker)的类型  o * . , x X + H 1 2 h P s v 3 4 D ^ < | d p > _
#ms 点的大小
#mec点的边缘颜色
#mfc点的内部颜色
#注意：颜色可以用简称、名称与16进制（#xxxxxx（#+六位））来表示
# 线(linestyle)  _   --   :   -.  none  solid dashdot
# color+name
# linewidth 线条宽度
F1={'family':'sans-serif','color':'blue','size':20}
#字体，颜色，大小
plt.title("图表名称",fontdict=F1,loc='left')
#loc设定标题位置，参数有left，right，center
plt.grid(color='green',linestyle='--',linewidth=1)
#grid生成网格，参数axis='x'可以设定只显示x向的

plt.xlabel("x轴名称")
plt.ylabel("y轴名称")
##plt.subplot一张图中可以有多张图




plt.show()
