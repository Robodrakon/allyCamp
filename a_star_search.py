# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:53:56 2020

@author: ajb22
"""


import networkx as nx 
import matplotlib.pyplot as plt
import queue
import random 

# create a 6x6 grid
K = nx.grid_2d_graph(6, 6)

# create positions of each node with a dictionary
pos = dict((n,n) for n in K.nodes())

# start and goal position
start = pos[(0, 0)]
goal = pos[(5, 5)]

# draw graph
nx.draw(K, pos=pos)
# label graph
nx.draw_networkx_labels(K, pos=pos, font_size = 22, font_color='r', font_weight='bold')
plt.show()

# implement breadth first search
# things that you will need to look up
#   - how to add something to a queue 
#   - how to get something from the queue
#   - how to get the neighboring nodes in network x grid (if I am in node (1,0) I want my neighbors to loop through (0,0), (2,0), (1,1)) 
# hint: your frontier will be queue.Queue()

# dictionary example 

# family = { 'Abby' : [23, 'girl'], 'Maddie' : [20, 'girl'], 'Evan' : [17, 'boy'], 'Dad' : [50, 'boy'], 'Mom' : [45, 'girl'], 'Ally' : [26, 'girl']}

# family
# Out[10]: 
# {'Abby': [23, 'girl'],
#  'Maddie': [20, 'girl'],
#  'Evan': [17, 'boy'],
#  'Dad': [50, 'boy'],
#  'Mom': [45, 'girl'],
#  'Ally': [26, 'girl']}

# family.keys()
# Out[11]: dict_keys(['Abby', 'Maddie', 'Evan', 'Dad', 'Mom', 'Ally'])

# family['Abby']
# Out[12]: [23, 'girl']

# family['Evan']
# Out[13]: [17, 'boy']
# Out[13]: [17, 'boy']

frontier = queue.Queue()
frontier.put(start)
visited = []
seen = []
seen.append(start)

while frontier.empty() == False:
    position = frontier.get()
    visited.append(position)
    for neighbor in K.neighbors(position):
        if neighbor not in seen:
            frontier.put(neighbor)
            seen.append(neighbor)
print(seen)

