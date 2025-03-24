#  Eulerian Path

##  Overview
This project demonstrates how to generate **random graphs** and determine whether they contain an **Eulerian Path** or **Eulerian Circuit**, using **Hierholzer's Algorithm**. It includes full visualization support using `networkx` and `matplotlib`.

Supports:
-  Directed or Undirected Graphs  
-  Optional Edge Weights  
-  Automatic seed search to guarantee Eulerian structure  

---

##  Features
-  **Random Graph Generation** (customizable size, edges, direction, weights)
-  **Connectivity Check** (Depth-First Search)
-  **Euler Path/Circuit Detection** (based on node degrees)
-  **Hierholzer’s Algorithm** for finding Eulerian paths/circuits
-  **Graph Visualization** using `networkx` and `matplotlib`
-  **Smart Seeding** (find seeds that guarantee a valid Eulerian graph)
---

```text
Generated Graph (Seed = 487974):
1: [(3, 4), (2, 5), (3, 7), (0, 1), (4, 7), (0, 8)]
3: [(1, 4), (1, 7)]
4: [(0, 4), (0, 5), (2, 1), (1, 7)]
0: [(4, 4), (4, 5), (1, 1), (1, 8), (2, 1)]
2: [(1, 5), (4, 1), (0, 1)]

Analysis:
Euler Path exists: True
Euler Circuit (circular) exists: False

Euler Path: [0, 2, 4, 1, 0, 4, 0, 1, 3, 1, 2]
Total cost of Euler path: 32
The Euler path is NOT a circuit (not circular)

Random Seed Used: 487974
