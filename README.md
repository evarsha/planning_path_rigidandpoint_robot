# Path Planning for a Rigid and Point Robot

ENPM661 Project_2

The libraries to be imported for executing the code:

1. import numpy as np

2. import math

3. import pygame

4. import sys


For running the given code, follow these steps:

1. Open the terminal in the saved folder location.

2. Then enter:
   - "python3 Dijkstra_point.py" for dijkstra algorithm of the point robot
   
   - "python3 Dijkstra_rigid.py" for dijkstra algorithm of the Rigid robot  
                 
   - "python3 A*_point.py" for Astar algorithm of the point robot
                 
   - "python3 A*_rigid.py" for Astar algorithm of the Rigid robot

3. Inputs should now be entered in the terminal.


Note:-

1. All the inputs have to be non negative integer numbers.

2. Resolution is for the purpose of GUI and node generation only, nodes should be entered in actual world as integers (x in between 0 and 250, y in between 0 and 150)

3. Make sure that the resolution entered does not give a floating point. (i.e., nodes_entered % resolution == 0)

