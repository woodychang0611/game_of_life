import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import random

# ImageMagick is needed for gif 
# ffmpeg is needed for avi

x_size = 50
y_size = 50
init_ratio =0.2

data = np.zeros((x_size,y_size))
new_data = np.zeros((x_size,y_size))
fig = plt.figure()
plt.axis('off')
plt.title('Game of Life')
ax=fig.gca()

im = ax.imshow(data,animated=True, vmin=0,vmax=6)

def init_data():
    global data
    for x in range(0,len(data[0])):
        for y in range(0,len(data)):
         if(random.random() < init_ratio):
              data[x,y]=1;

def health_neighbors(x,y,data):
    count =0
    for x_det in range(-1,2):
        for y_det in range(-1,2):
            if(y+y_det<0 or x+x_det<0):
                continue
            if(x_det == 0 and y_det==0):
                continue
            if(y+y_det>=y_size or x+x_det>=x_size):
                continue
            if data[x+x_det,y+y_det] >=1:
                count +=1
    return count;

def update_data():
    global data
    global new_data
    new_data.fill(0)
    for x in range(0,x_size):
        for y in range(0,y_size):
            new_data[x,y] =0
            a = new_data[x,y];
            number_neighbors = health_neighbors(x,y,data)
            if number_neighbors >3 or number_neighbors <2:
                pass
            elif data[x,y]>0 or number_neighbors ==3:
                new_data[x,y]=data[x,y]+1
    data = new_data.copy()

def update_frame(frame):
    global data
    if(frame>5):
        update_data()
    im.set_data(data)
    ax.set_title("Frame:{0}".format(frame))
    return im
    
animation = FuncAnimation(fig, update_frame, interval=100,frames=500,init_func=init_data )
animation.save("game_of_life.avi")
animation.save("game_of_life.gif",writer='imagemagick',fps=15)
plt.show()
exit()
