#  Eulerian Path & Circuit Visualizer

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

## 🖼 Visualization Example

| Original Graph | Eulerian Path Highlighted |
|----------------|---------------------------|
| ![Original Graph](images/original.png) | ![Eulerian Path](images/euler-path.png) |

*(Note: Images are generated at runtime and not included by default.)*
