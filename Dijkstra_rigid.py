#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys


# In[2]:


import math
import pygame


# In[3]:


def up(current_node):
    new_node=[current_node[0], current_node[1]-1]
    cost=1
    return new_node,cost

def up_right(current_node):
    new_node=[current_node[0]+1, current_node[1]-1]
    cost=math.sqrt(2)
    return new_node,cost

def right(current_node):
    new_node=[current_node[0]+1, current_node[1]]
    cost=1
    return new_node,cost


def down_right(current_node):
    new_node=[current_node[0]+1, current_node[1]+1]
    cost=math.sqrt(2)
    return new_node,cost


def down(current_node):
    new_node=[current_node[0], current_node[1]+1]
    cost=1
    return new_node,cost


def down_left(current_node):
    new_node=[current_node[0]-1, current_node[1]+1]
    cost=math.sqrt(2)
    return new_node,cost

def left(current_node):
    new_node=[current_node[0]-1, current_node[1]]
    cost=1
    return new_node,cost

def up_left(current_node):
    new_node=[current_node[0]-1, current_node[1]-1]
    cost=math.sqrt(2)
    return new_node,cost


# In[4]:


def append(child_list,parent_list,cost,x,parent_node,child_node,child_cost):
    lst=range(0,len(child_list))
    lst=lst[::-1]
    flag=0
    for cku in lst:
        if(child_node == child_list[cku]):
            flag=1
            if(cost[cku]>=(cost[x]+child_cost)):
                parent_list[cku]=parent_node
                cost[cku]=round((cost[x]+child_cost),1)
                break
                    
                    
    if (flag!=1):
        parent_list.append(parent_node)
        child_list.append(child_node)
        cost.append(round((child_cost+cost[x]),1))
    
    return child_list,parent_list,cost


# In[5]:


print("Enter robot parameters")
rad=float(input("radius =  "))
clr=float(input("clearence =  "))
def workspace(x,y,d=rad+clr):
    line1=(6525/25) - d*math.sqrt((-41/25)**2+1)
    line2=d*math.sqrt((-2/19)**2+1)+(1314/19)
    line3=d*math.sqrt((38/7)**2+1)-(5830/7)
    line4=-(6101/20)-d*math.sqrt((37/20)**2+1)
    line5= d*math.sqrt((-38/23)**2+1) + (8530/23)
    line6l= (6551/10)- d*math.sqrt((-37/10)**2+1)
    line6r=  d*math.sqrt((-37/10)**2+1) +(6551/10)
    o = 0
    if (x<(d/r))or (x>(250-d)/r) or (y<(d/r)) or (y>(150-d)/r):
        o=1
    if ((x-math.ceil(190/r))**2+(y-math.ceil(130/r))**2-(math.ceil((15+d)/r))**2)<0:
        o=1
    if ((2/19)*x + y - line2/r < 0) and (y+(41/25)*x -line1/r > 0) and (y - ((15-d)/r)> 0) and (y<(-37/10)*x+line6r/r):
        o=1
    if ((-38/7)*x +y - line3/r < 0) and ((38/23)*x + y - line5/r < 0) and (y - ((15-d)/r) > 0) and ((-37/20)*x +y -line4/r > 0) and (y>(-37/10)*x+line6l/r):
        o=1
    if (x-math.floor((50-d)/r) > 0) and (x - math.floor((100+d)/r) < 0) and (y - math.floor((67.5-d)/r) > 0) and (y - math.floor((112.5+d)/r) < 0):
        o=1
    if ((x-math.ceil(140/r))/(math.ceil(15+d)/r))**2 + ((y - math.ceil(120/r))/(math.ceil(6+d)/r))**2 - 1 < 0:
        o=1
    return o


# In[6]:


print("Enter the starting node coordinates")
xi=float(input("x =  "))
yi=float(input("y =  "))
ndi=[xi,yi]
print("Enter the goal node coordinates")
xg=float(input("x =  "))
yg=float(input("y =  "))
goal=[xg,yg]
r=int(input("Enter the desired Resolution (an integer value) =  "))
goal= [n / r for n in goal]
ndi=[m / r for m in ndi]
parent_list=[ndi]
child_list=[ndi]
visited_pn=[]
visited_cn=[]
visited_cost=[]
rows=150/r
coloums=250/r

if (workspace(goal[0],goal[1])==1 or workspace(ndi[0],ndi[1])):
    sys.exit("The given nodes happen to lie in the obstacle space 'or' outside the workspace")

if (ndi[0] not in range(0,251) or goal[0] not in range(0,251) or ndi[1] not in range(0,151) or goal[1] not in range(0,151)):
    sys.exit("The given nodes are not integers 'or' lie outside the workspace 'or' invalid resolution was given")

x=0
cost=[0]
parent_node=ndi
check=0


while(check!=1 and child_list!=[]):
    
    #--- UP Command ---
    child_node,child_cost=up(parent_node)
    if (child_node[1]>=0 and workspace(child_node[0],child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node,child_cost)
            
            
    #--- DOWN Command ---
    child_node,child_cost=down(parent_node)
    if (child_node[1]<=rows and workspace(child_node[0],child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node, child_cost)
            
            
    #--- LEFT Command ---
    child_node,child_cost=left(parent_node)
    if (child_node[0]>=0 and workspace(child_node[0],child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node,child_cost)


    #--- RIGHT Command ---
    child_node,child_cost=right(parent_node)
    if (child_node[0]<=coloums and workspace(child_node[0],child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node,child_cost)
            
    #--- UP LEFT Command ---
    child_node,child_cost=up_left(parent_node)
    if (child_node[1]>=0 and child_node[0]>=0 and workspace(child_node[0],child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node,child_cost)
            
    #--- UP RIGHT Command ---
    child_node,child_cost=up_right(parent_node)
    if (child_node[0]<=coloums and child_node[1]>=0 and workspace(child_node[0],child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node,child_cost)


            
    #--- DOWN LEFT Command ---
    child_node,child_cost=down_left(parent_node)
    if (child_node[1]<=rows and child_node[0]>=0 and workspace(child_node[0], child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node,child_cost)
            
    #--- DOWN RIGHT Command ---
    child_node,child_cost=down_right(parent_node)
    if (child_node[1]<=rows and child_node[0]<=coloums and workspace(child_node[0],child_node[1])!=1):
        if child_node not in visited_cn:
            child_list,parent_list,cost=append(child_list,parent_list,cost,x,parent_node,child_node,child_cost)
    
    prnt_node=parent_list.pop(x)
    visited_pn.append(prnt_node)
    chld_node=child_list.pop(x)
    visited_cn.append(chld_node)
    cst_vistd=cost.pop(x)
    visited_cost.append(cst_vistd)

    if(visited_cn[-1]==goal):
        check=1
        
    if(check!=1):
        x=cost.index(min(cost))
        parent_node=child_list[x][:]

if(check==0 and child_list==[]):
    sys.exit("Path Does not exist")
    
seq=[]
seq.append(visited_cn[-1])
seq.append(visited_pn[-1])
x=visited_pn[-1]
i=1
while(x!=ndi):
    if(visited_cn[-i]==x):
        seq.append(visited_pn[-i])
        x=visited_pn[-i]
    i=i+1      


#print("\n Sequence = ",seq)


# In[7]:


obs_space = []
for i in range(0,251):
    for j in range(0,151):
        q=workspace(i,j)
        if q == 1:
            obs_space.append([i,j])

k=2
my_list = np.array(visited_cn)
visited_cn=my_list*k*r
my_list1 = np.array(seq)
seq=my_list1*k*r
my_list2 = np.array(obs_space)
obs_space = my_list2*k*r


pygame.init()

#Defining the colors
Black = [0, 0, 0]
red = [255, 0, 0]
green = [0, 255, 0]
White = [255, 255, 255]

#Height and Width of Display
SIZE = [250*k+r+r, 150*k+r+r]
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("OUTPUT")
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
 
    screen.fill(Black)
#Printing the obstacles
    for i in obs_space:
        pygame.draw.rect(screen, green, [i[0],150*k-i[1],r*k,r*k])
    pygame.display.flip()
    clock.tick(20)
#Printing the visited nodes
    for i in visited_cn:
        pygame.time.wait(1)
        pygame.draw.rect(screen, White, [i[0],150*k-i[1],r*k,r*k])
        pygame.display.flip()
#Printing the path
    for j in seq[::-1]:
        pygame.time.wait(1)
        pygame.draw.rect(screen, red, [j[0], 150*k-j[1], r*k,r*k])
        pygame.display.flip()
    pygame.display.flip()

    pygame.time.wait(1500)
    done = True
pygame.quit()


# In[ ]:




