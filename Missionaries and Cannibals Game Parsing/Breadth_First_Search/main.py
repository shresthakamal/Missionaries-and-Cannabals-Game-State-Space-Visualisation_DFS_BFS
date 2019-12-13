from time import time
from Breadth_First_Search import bfs
from Level_Nodes import Node

initial_state= [3,3,1]

Node.num_of_instances=0
t0=time()
dfs=bfs(initial_state)
t1=time()-t0
print('Represented Nodes:', dfs)
print('Space Complexity:',Node.num_of_instances)
print('Time Taken:',t1)
