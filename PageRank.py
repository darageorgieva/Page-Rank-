import networkx as nx
import numpy as np
import sys 

fh=open(sys.argv[1], "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())
fh.close()

iterations = 20

m = 0.15 # damping factor
n = len(G) # number of nodes

x_k = np.ones(n) / n # initial rank vector - an array of 1s with the size of n
# here we are not creating the whole matrix A (n by n) for optimization purposes

mSx_k = np.full(n, m/n) # an array of size n filled with value m/n, responsible for random jumping
# again not creating the whole matrix since all its values are the same 

# append the node to the dangling nodes list if it has no outlinks to sucessors (its out_degree is 0)
dangling_nodes = [node for node in G.nodes() if G.out_degree(node) == 0] 

#print(f"Dangling nodes: {dangling_nodes} (Total: {len(dangling_nodes)})")

# creating this dictionary with nodes as keys and their indexes as values and filling it up as nodes in G appear
# so we can correctly perform operations with them
node_index = {node: i for i, node in enumerate(G.nodes())}

for iteration in range(iterations):
    x_k_1 = np.zeros(n)
    D_x_k = (1 - m) * np.sum([x_k[node_index[node]] for node in dangling_nodes]) / n 
    # we compute the constant D_x_k once for every iteration 
    for node in G.nodes():
        for predecessor in G.predecessors(node):
            outlinks_predecessor = G.out_degree(predecessor)
            weight_from_predecessor = (1 - m) * x_k[node_index[predecessor]] / outlinks_predecessor
            x_k_1[node_index[node]] += weight_from_predecessor
            # to each element in the x_k_1 array representing the importance score of the node
            # add weight from the predecessor
    
    # to get the true importance score we sum the weights from predecessors, random jumping and dangling nodes
    x_k_1 = x_k_1 + mSx_k + D_x_k

    #check if convergence is reached
    if np.linalg.norm(x_k - x_k_1) < 1e-6:
        print(f"This took {iteration + 1} iterations.")
        break
    

    # convergence has not been reached yet so we update x_k for the next iteration
    # eigenvalue lambda for pagerank is 1 so Av = v so in our case we assign x_k_1 to become x_k and new iteration begins
    x_k = x_k_1 

print(f'Importance vector after {iteration + 1} iterations is {x_k}')

x_k_dict = {node: float(x_k[node_index[node]]) for node in G.nodes()}
x_k_dict_sorted = dict(sorted(x_k_dict.items(), key=lambda item: item[1], reverse=True))


top10_nodes = list(x_k_dict_sorted.items())[:10]

for rank, (node, score) in enumerate(top10_nodes, start=1):
    print(f"#{rank}: Node {node} - Score: {score}")




