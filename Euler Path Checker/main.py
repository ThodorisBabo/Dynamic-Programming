import random
from collections import defaultdict, deque
import matplotlib.pyplot as plt
import networkx as nx

# Step 1: Generate a random undirected or directed graph with optional weights
def generate_graph(num_vertices=6, num_edges=8, directed=False, weighted=False):
    graph = defaultdict(list)
    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v and ((u, v) not in edges if directed else (u, v) not in edges and (v, u) not in edges):
            weight = random.randint(1, 10) if weighted else 1
            edges.add((u, v, weight))
            graph[u].append((v, weight))
            if not directed:
                graph[v].append((u, weight))
    return graph, list(edges)

# Step 2: Check if graph is connected
def is_connected(graph):
    visited = set()
    nodes = list(graph.keys())
    if not nodes:
        return True

    def dfs(v):
        visited.add(v)
        for neighbor, _ in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(nodes[0])
    for node in graph:
        if graph[node] and node not in visited:
            return False
    return True

# Step 3: Check degrees for Euler path/circuit (undirected)
def has_euler_path(graph):
    odd = 0
    for node in graph:
        if len(graph[node]) % 2 != 0:
            odd += 1
    return (odd == 0 or odd == 2) and is_connected(graph)

def has_euler_circuit(graph):
    for node in graph:
        if len(graph[node]) % 2 != 0:
            return False
    return is_connected(graph)

# Step 4: Hierholzer's Algorithm to find Eulerian Path or Circuit
def find_eulerian_path(graph):
    graph_copy = defaultdict(list)
    for u in graph:
        for v, _ in graph[u]:
            graph_copy[u].append(v)

    start = next((u for u in graph_copy if len(graph_copy[u]) % 2 == 1), next(iter(graph_copy)))
    stack = [start]
    path = []

    while stack:
        u = stack[-1]
        if graph_copy[u]:
            v = graph_copy[u].pop()
            graph_copy[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())
    return path[::-1]

# Step 5: Visualize the graph using NetworkX with subplots
def visualize_graph(edges, path=None, directed=False):
    G1 = nx.DiGraph() if directed else nx.Graph()
    G2 = nx.DiGraph() if directed else nx.Graph()
    G1.add_weighted_edges_from(edges)
    G2.add_weighted_edges_from(edges)
    pos1 = nx.spring_layout(G1)
    pos2 = pos1.copy()

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    edge_labels = {(u, v): w for u, v, w in edges}

    # Original Graph
    nx.draw(G1, pos1, with_labels=True, node_color='skyblue', node_size=1000, edge_color='gray', width=2, font_size=14, ax=axs[0])
    nx.draw_networkx_edge_labels(G1, pos1, edge_labels=edge_labels, ax=axs[0])
    axs[0].set_title("Original Graph")

    # Euler Path Highlighted
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw(G2, pos2, with_labels=True, node_color='lightgreen', node_size=1000, edge_color='gray', width=2, font_size=14, ax=axs[1])
        nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels, ax=axs[1])
        nx.draw_networkx_edges(G2, pos2, edgelist=path_edges, edge_color='red', width=3, ax=axs[1])
        axs[1].set_title("Euler Path Highlighted")
    else:
        nx.draw(G2, pos2, with_labels=True, node_color='lightcoral', node_size=1000, edge_color='gray', width=2, font_size=14, ax=axs[1])
        nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels, ax=axs[1])
        axs[1].set_title("No Euler Path Found")

    plt.tight_layout()
    plt.show()

# Step 6: Find a seed with an Euler path or circuit
def find_valid_seed(num_nodes, num_edges, directed, weighted, require_circuit=False, max_attempts=10000):
    for attempt in range(max_attempts):
        seed = random.randint(0, 1000000)
        random.seed(seed)
        graph, _ = generate_graph(num_nodes, num_edges, directed, weighted)
        if require_circuit and has_euler_circuit(graph):
            return seed
        elif not require_circuit and has_euler_path(graph):
            return seed
    return None

# Step 7: Main
if __name__ == "__main__":
    DIRECTED = False
    WEIGHTED = True
    NUM_NODES = 5
    NUM_EDGES = NUM_NODES * 2
    FIND_VALID_SEED = True
    REQUIRE_CIRCUIT = False

    if FIND_VALID_SEED:
        seed = find_valid_seed(NUM_NODES, NUM_EDGES, DIRECTED, WEIGHTED, REQUIRE_CIRCUIT)
        if seed is None:
            print("Could not find a valid seed with the required conditions.")
            exit()
    else:
        seed = random.randint(0, 1000000)

    random.seed(seed)
    graph, edges = generate_graph(num_vertices=NUM_NODES, num_edges=NUM_EDGES, directed=DIRECTED, weighted=WEIGHTED)
    print("Generated Graph (Seed = {}):".format(seed))
    for u in graph:
        print(f"{u}: {graph[u]}")

    print("\nAnalysis:")
    euler_path_exists = has_euler_path(graph)
    euler_circuit_exists = has_euler_circuit(graph)

    print("Euler Path exists:", euler_path_exists)
    print("Euler Circuit (circular) exists:", euler_circuit_exists)

    if euler_path_exists:
        path = find_eulerian_path(graph)
        print("\nEuler Path:", path)
        total_weight = 0
        for i in range(len(path) - 1):
            for v, w in graph[path[i]]:
                if v == path[i+1]:
                    total_weight += w
                    break
        print("Total cost of Euler path:", total_weight)

        if path[0] == path[-1]:
            print("The Euler path is a CIRCUIT (circular)")
        else:
            print("The Euler path is NOT a circuit (not circular)")
        visualize_graph(edges, path, directed=DIRECTED)
    else:
        print("\nNo Euler Path found in this graph.")
        visualize_graph(edges, directed=DIRECTED)

    print(f"\nRandom Seed Used: {seed}")
