import networkx as nx
import numpy as np
import random
import sys 

fh=open(sys.argv[1], "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())
fh.close()


nodes = list(G.nodes())
visit_counts = {node: 0 for node in nodes} # at first every node has 0 visits 

m = 0.15
steps = 5000000

current_node = random.choice(nodes) # pick a random inital node

for _ in range(steps): # start surfing 
    visit_counts[current_node] += 1  # count visit for the current node
    p = random.random() # for each step generate a random probability of surfing to another page

    if p < m: # if this probability is less that the damping factor m jump to a random node 
        current_node = random.choice(nodes)
    else: # but if the probability is equal or greater than m randomly follow a link or at least attempt to do so (dangling nodes exist)
        successors = list(G.successors(current_node))
        if successors: # if there are outgoing links to other nodes, pick randomly from them
            current_node = random.choice(successors)
        else: # if no outgoing edges (dangling node), jump to a random node
            current_node = random.choice(nodes)
    


# printing the 10 most visited by sorting by the values in the dictionary in descending order
# then slicing for top 10
top10_sorted_visits = sorted(visit_counts.items(), key=lambda item: item[1], reverse=True)[:10]

for rank, (node, visits) in enumerate(top10_sorted_visits, start = 1):
    print(f"#{rank}: Node {node} - Visits: {visits}")