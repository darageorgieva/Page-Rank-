# PageRank Implementation - README

## Project Overview
This project implements the **PageRank algorithm**, a ranking system used by Google to assign a numerical value to webpages based on their importance. The PageRank algorithm can be understood as a random surfer model, where each page is visited randomly, and the more frequently a page is visited, the higher its importance. This implementation also demonstrates how to calculate eigenvectors, handle sparse matrices, and compute approximations of eigenvectors for large graphs.

## Objectives
1. Implement the PageRank algorithm using a random surfer model.
2. Compute the importance scores of nodes in a directed graph.
3. Handle large graphs efficiently using sparse matrix representations.
4. Validate the implementation with real-world datasets, including the Gnutella graph.

## Deliverables
- **Source Code:** Python code for both the random surfer simulation and PageRank computation.
- **Results:** Output of the top 10 most visited nodes from the random surfer and the top 10 highest ranking nodes from the PageRank algorithm.
- **Convergence Data:** Number of iterations required for the PageRank algorithm to stabilize.

## Getting Started

### Prerequisites
To run the project in Python, the following libraries are required:
- `networkx` for graph representation.
- `numpy` for matrix manipulation.

Install them using pip:
pip install networkx numpy

### Setup
1. Clone or download this repository.
2. Place the dataset files in the same directory as the Python script.
3. Ensure that you have the necessary datasets for testing (such as the Gnutella graph) from the course learnit page.

### Usage
1. **Random Surfer Simulation:** 
   - Run the `pagerank.py` script with the desired dataset file as an argument.
   - The random surfer simulation will run, and the 10 most visited nodes will be printed.
   
   Example command:
   ```bash
   python pagerank.py gnutella_data.txt
# PageRank Algorithm Implementation

## Overview
This project implements the **PageRank algorithm**, a ranking system used by Google to determine the importance of webpages. It leverages the eigenvector of a matrix `M`, where `M` is a transition matrix derived from the web graph. The algorithm is a core part of understanding how link structures influence ranking and can be computed through both random walk models and linear algebraic methods.

## PageRank Algorithm

The script computes the importance scores of the nodes in the graph using the PageRank algorithm. The output includes:

- **Top 10 nodes with the highest importance scores.**
- **The number of iterations required for the PageRank algorithm to stabilize.**

### My Output

Results for the Gnutella graph:
Results from Page Rank:
This took 9 iterations.
Importance vector after 9 iterations is [0.00010058 0.00010913 0.000171 ... 0.00011186 0.00011186 0.00011186]
#1: Node 367 - Score: 0.002387650830015758
#2: Node 249 - Score: 0.0021842951424048836
#3: Node 145 - Score: 0.0020548859393247436
#4: Node 264 - Score: 0.001998749916194164
#5: Node 266 - Score: 0.0019634403057468266
#6: Node 123 - Score: 0.0018634931279900315
#7: Node 127 - Score: 0.0018605110789676085
#8: Node 122 - Score: 0.0018532460701586075
#9: Node 1317 - Score: 0.001843504657081592
#10: Node 5 - Score: 0.001831073888467343
Results from Random Surfer:
#1: Node 367 - Visits: 11995
#2: Node 249 - Visits: 10795
#3: Node 264 - Visits: 10212
#4: Node 145 - Visits: 10160
#5: Node 266 - Visits: 9853
#6: Node 123 - Visits: 9406
#7: Node 1317 - Visits: 9391
#8: Node 127 - Visits: 9377
#9: Node 122 - Visits: 9247
#10: Node 5 - Visits: 9074

## Conclusion:

*   The experiment demonstrates that while the **Random Surfer model** can provide an approximation of node importance based on visit frequency, the **PageRank algorithm** is a much more accurate and stable method for ranking nodes. PageRank accounts for the **link structure**, the **influence** of other nodes, and converges to a stable set of importance scores after just a few iterations.
  
*   The **PageRank algorithm** delivers **mathematically rigorous** and **reliable rankings**, which is why it is employed by systems like Google for web page ranking.

