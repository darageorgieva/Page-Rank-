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

### Example Output

```yaml
Top 10 Most Visited Nodes (Random Surfer Simulation):
1. Node 45: 500 visits
2. Node 12: 490 visits
...

Top 10 Highest Ranking Nodes (PageRank Algorithm):
1. Node 45: 0.12
2. Node 12: 0.11
...

Number of Iterations for PageRank to Stabilize: 35
