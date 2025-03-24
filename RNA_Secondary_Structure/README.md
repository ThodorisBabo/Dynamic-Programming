# RNA Secondary Structure Prediction

## Overview
This project focuses on predicting the **secondary structure of RNA sequences** using **Dynamic Programming**. The approach follows the **Nussinov algorithm**, which identifies **optimal base pairings** to determine the most stable RNA fold.

## Features
- **Base Pair Detection:** Identifies valid **(A-U, C-G)** base pairs.
- **Dynamic Programming Optimization:** Implements the **Nussinov algorithm** to compute the optimal RNA secondary structure.
- **Dot-Bracket Notation:** Converts base-pair mappings into a standard **dot-bracket format** for visualization.
- **Efficient Computation:** Uses a **bottom-up DP approach** to optimize runtime.
- **Result Visualization:** Outputs **dot-bracket notation** and base pairings for structure visualization.

## Input & Output

### Input
- A string representing an **RNA sequence** composed of characters: `A`, `U`, `C`, and `G`.
- Example: AAGACUUCGGAUCUGGCGACACCC

### Output

- **Sorted Base Pairs** (as index positions):
[(0, 13), (2, 12), (3, 11), (4, 9), (14, 22), (15, 21)]
- **Base Pairings** (nucleotide-level):
[('A', 'U'), ('G', 'C'), ('A', 'U'), ('C', 'G'), ('G', 'C'), ('G', 'C')]
- **Dot-Bracket Notation** (RNA secondary structure):
(.(((....).)))((.....)).

