# ============================================================
# AI Practical 1 : DFS and BFS on an undirected graph
# ============================================================
# Problem statement:
# Implement Depth First Search (DFS) and Breadth First Search (BFS).
# Use an undirected graph and develop a recursive algorithm for
# searching all the vertices of a graph or tree data structure.
#
# Based on the SPPU TE Comp Content repository (KSKA Git).
# Minor changes for the lab:
#   - clearer input prompts (enter ONE vertex per line)
#   - main() is called only when this file is run directly
# ============================================================

from collections import deque


class Graph:
    # Constructor to initialize an empty dictionary
    def __init__(self):
        self.graph = {}

    # Add edges
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph.
        # For a directed graph, comment out the line above.

    # Depth First Search (recursive)
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbour in self.graph.get(start, []):
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    # Breadth First Search (queue + recursive helper)
    def bfs(self, start):
        visited = set()
        visited.add(start)
        queue = deque([start])

        def bfs_helper():
            if not queue:
                return

            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbour in self.graph.get(vertex, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

            bfs_helper()

        bfs_helper()


def main():
    g = Graph()

    while True:
        print("\n\n", "-" * 10, "MAIN MENU", "-" * 10)
        print("1. Add edge")
        print("2. Depth First Search (DFS)")
        print("3. Breadth First Search (BFS)")
        print("4. Exit")
        choice = int(input("Choose an option (1-4):\t"))
        print("-" * 32)

        if choice == 1:
            total = int(input("\nTotal edges to add:\t"))
            for i in range(total):
                print(f"EDGE {i + 1} ->")
                print("(Enter ONE vertex name per line.)")
                u = input(f"Enter first vertex for edge {i + 1}: ").strip()
                v = input(f"Enter second vertex for edge {i + 1}: ").strip()
                g.add_edge(u, v)
            print("\nVertices and their neighbours are:\t", g.graph)

        elif choice == 2:
            start = input("\nEnter starting vertex for DFS:\t").strip()
            print("Depth First Search (DFS):\t", end="")
            g.dfs(start)
            print()

        elif choice == 3:
            start = input("\nEnter starting vertex for BFS:\t").strip()
            print("Breadth First Search (BFS):\t", end="")
            g.bfs(start)
            print()

        elif choice == 4:
            print("\n## END OF CODE\n")
            break

        else:
            print("\nPlease choose a valid option.")


if __name__ == "__main__":
    main()
