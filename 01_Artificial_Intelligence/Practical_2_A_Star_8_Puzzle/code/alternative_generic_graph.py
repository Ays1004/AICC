# Assignment-A2 (A* Algorithm)

"""
THIS CODE HAS BEEN TESTED AND IS FULLY OPERATIONAL.

Problem Statement: Implement A star Algorithm for any game search problem.

Code from ArtificialIntelligence (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/ArtificialIntelligence
"""

# This code directly implements A* algorithm for finding the optimal
# solution. It is NOT implemented for any game search problem.

# A* implementation for 8 puzzle problem can be found in the "Codes" folder
# and maze problem solving can be found in the "Alternatives" folder.

# BEGINNING OF CODE
import heapq

def a_star(graph, start, goal, heuristic):
    g = {v: float('inf') for v in graph}
    f = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}

    g[start] = 0
    f[start] = heuristic[start]

    open_list = [(f[start], start)]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(parent, goal, g[goal])

        for neighbor, weight in graph[current]:
            tentative_g = g[current] + weight
            if tentative_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f[neighbor], neighbor))

    return []

def reconstruct_path(parent, goal, cost):
    path = []
    while goal:
        path.append(goal)
        goal = parent[goal]
    path.reverse()
    print("Path cost:", cost)
    return path

def main():
    n = int(input("Enter number of vertices: "))
    print("Enter vertex names (e.g., A B C ...):")
    vertices = input().split()

    graph = {v: [] for v in vertices}

    m = int(input("Enter number of edges: "))
    print("Enter edges (format: source destination weight):")
    for _ in range(m):
        u, v, w = input().split()
        w = int(w)
        graph[u].append((v, w))
        # graph[v].append((u, w))  # Uncomment for undirected graph

    heuristic = {}
    print("Enter heuristic values (e.g., A 4 B 2 ...):")
    for _ in range(n):
        name, h = input().split()
        heuristic[name] = int(h)

    start = input("Enter start vertex: ")
    goal = input("Enter goal vertex: ")

    path = a_star(graph, start, goal, heuristic)
    if path:
        print("Optimal path:", ' -> '.join(path))
    else:
        print("No path found.")

main()
# END OF CODE
