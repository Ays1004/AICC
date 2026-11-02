# Assignment-A1 (DFS | BFS) -> Alternative

"""
THIS CODE HAS BEEN TESTED AND IS FULLY OPERATIONAL.

Problem Statement: Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

Code from ArtificialIntelligence (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/ArtificialIntelligence
"""

# Uses queue for BFS & stack for DFS

# BEGINNING OF CODE
def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]

    while queue:
        node = queue.pop(0)
        if not visited[node]:
            print(node, end=" ")
            visited[node] = True

            for neighbour in range(len(graph)):
                if graph[node][neighbour] == 1 and not visited[neighbour]:
                    queue.append(neighbour)

def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        node = stack.pop()
        if visited[node] != True:
            print(node, end=" ")
            visited[node] = True

            for neighbour in range(len(graph) - 1, -1, -1):
                if  graph[node][neighbour] == 1 and visited[neighbour] != True:
                    stack.append(neighbour)

graph = [
    # A  B  C  D  E  F
    [ 0, 1, 1, 0, 0, 0], # A
    [ 1, 0, 0, 1, 1, 0], # B
    [ 1, 0, 0, 0, 0, 1], # C
    [ 0, 1, 0, 0, 0, 0], # D
    [ 0, 1, 0, 0, 0, 1], # E
    [ 0, 0, 1, 0, 1, 0]  # F
] # Might need to take user input for this. Hard coded values only for testing.

print("Breadth First Search:\t", end=" ")
bfs(graph, 0)
print("\nDepth First Search:\t", end=" ")
dfs(graph, 0)
# END OF CODE
