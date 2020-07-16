# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:57:18 2020

@author: ajb22
"""

import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt
import random

random.seed(0)

G = nx.DiGraph()


node_name = 1

for i in range(3):
    for j in range(4):
        G.add_node(str(node_name))
        
        if j == 0:
            G.add_edge("0", str(node_name))
            #G.add_edge(str(node_name), "0")
        else:
            G.add_edge(str(node_name-1), str(node_name))
            #G.add_edge(str(node_name), str(node_name-1))
        node_name += 1
        

labels = {}
for node in G.nodes:
    # assigning random costs to the nodes
    # G.nodes[node]['cost'] = random.randint(1,50)
    labels[node] = node
    
G.add_edge("6", "11")
    
# write dot file to use with graphviz
# run "dot -Tpng test.dot >test.png"
write_dot(G,'test.dot')

# same layout using matplotlib with no labels
plt.title('draw_networkx')

pos =graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=False, arrows=True)
nx.draw_networkx_labels(G, pos=pos, labels=labels, font_size = 22, font_color = 'k', font_weight = 'bold')
plt.show()
plt.savefig('nx_tree.png')

#############################################################################
# solution #


            

        
    

