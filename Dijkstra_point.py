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


def workspace(wx, wy):
           
    o = 0
            
    if (wx-math.floor(50/r) >= 0) and (wx - math.floor(100/r) <= 0) and (wy - math.floor(67.5/r) >= 0) and (wy - math.floor(112.5/r) <= 0):
        o = 1
                
    elif ((wx-math.ceil(140/r))/math.ceil(15/r))**2 + ((wy - math.ceil(120/r))/math.ceil(6/r))**2 - 1 <=0:
        o = 1
                
    elif ((wx-math.ceil(190/r))**2 + (wy-math.ceil(130/r))**2-(math.ceil(15/r))**2) <= 0:
        o = 1
               
    elif ( 38*wx - 7*wy - 5830/r ) >= 0 and ( 38*wx + 23*wy - 8530/r ) <= 0 and ( 37*wx - 20*wy - 6101/r ) <= 0 and ( 37*wx + 10*wy - 6551/r ) >= 0:
        o = 1    
                    
    elif ( 2*wx + 19*wy - 1314/r ) <= 0 and ( 41*wx + 25*wy - 6525/r ) >= 0 and ( wy - 15/r ) >= 0 and ( 37*wx + 10*wy - 6551/r ) <= 0:
        o = 1
      
    return o


# In[9]:


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

while(check!=1):
    
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




