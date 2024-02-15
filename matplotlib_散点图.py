import matplotlib.pyplot as plt
import numpy as np

x=[1,1,4,5,1,4]
y=[1,9,1,9,8,1]
c=['red','red','blue','blue','pink','pink']
plt.scatter(x,y,color=c,s=range(1,7),alpha=0.5) #或者color=''
#s设定尺寸，alpha设定透明度


plt.show()
