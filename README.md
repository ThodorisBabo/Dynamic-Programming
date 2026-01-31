# Algorithmic Projects

## Overview

This repository contains **two algorithm-focused projects** that demonstrate the application of **graph theory** and **dynamic programming** to solve classical problems in computer science and computational biology. The projects emphasize **algorithmic correctness, efficiency, and visualization**, implemented in **Python**.

Together, they showcase techniques for **graph traversal and path finding** as well as **sequence optimization and structure prediction**.

---

## 1. Eulerian Path in Random Graphs

### Description

This project explores the generation and analysis of **random graphs** to determine whether they contain an **Eulerian Path** or an **Eulerian Circuit**. It uses **Hierholzer’s Algorithm** to construct valid Eulerian traversals when they exist and provides full graph visualization support.

### Key Features

* Random **directed or undirected graph generation**
* Optional **edge weights**
* **Connectivity checking** using Depth-First Search (DFS)
* Eulerian Path and Circuit detection based on **vertex degree conditions**
* Implementation of **Hierholzer’s Algorithm**
* **Graph visualization** using `networkx` and `matplotlib`
* **Smart seed search** to guarantee Eulerian graph structures

### Outcome

The program reports whether an Eulerian Path or Circuit exists, outputs the computed traversal, calculates its total cost, and visualizes the generated graph for intuitive understanding.

---

## 2. RNA Secondary Structure Prediction

### Description

This project focuses on predicting the **secondary structure of RNA sequences** using **Dynamic Programming**. It implements the **Nussinov algorithm** to identify optimal base pairings that maximize structural stability.

### Key Features

* Detection of valid RNA base pairs (**A–U, C–G**)
* **Bottom-up dynamic programming** implementation of the Nussinov algorithm
* Optimization for efficient computation
* Conversion of base-pair mappings into **dot-bracket notation**
* Clear output of base-pair indices and nucleotide-level pairings

### Input & Output

* **Input:** An RNA sequence consisting of `A`, `U`, `C`, and `G`
* **Output:**

  * Sorted base-pair index positions
  * Corresponding nucleotide base pairs
  * RNA secondary structure in **dot-bracket notation**

### Outcome

The project produces a compact and interpretable representation of RNA folding, making it suitable for educational purposes and as a foundation for more advanced bioinformatics tools.

---

## Technologies Used

* **Python**
* **NetworkX**
* **Matplotlib**
* Standard Python data structures and algorithms

---

## Summary

These projects demonstrate strong fundamentals in **algorithm design and analysis**, covering both **graph algorithms** and **dynamic programming for biological sequence analysis**. They are well-suited for academic coursework, algorithm practice, and as building blocks for more advanced research or applications.
