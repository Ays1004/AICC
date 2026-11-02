# Assignment-3.V (Prim's Minimal Spanning Tree Algorithm)

"""
THIS CODE HAS BEEN TESTED AND IS FULLY OPERATIONAL.

Problem Statement: Implement Greedy search algorithm for any of the following application:
  V. Prim's Minimal Spanning Tree Algorithm

Code from ArtificialIntelligence (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/ArtificialIntelligence
"""

# BEGINNING OF CODE
graph = []
def prims_mst(graph):
    n = len(graph)
    selected = [False] * n
    no_of_edges = 0
    selected[0] = True

    print("Edge : Weight")
    while no_of_edges < n - 1:
        minimum = 999
        x = 0
        y = 0

        for i in range(n):
            if selected[i]==True:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 999 and i != j:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        no_of_edges += 1

def input_graph():
    V = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix of Graph row by row:")
    for i in range(V):
        row = list(map(int, input(f"Row {i}: ").split()))
        graph.append(row)
def main():
	while True:
        	print("\nMenu:")
        	print("1. Input graph")
        	print("2. Run Prim's MST algorithm")
        	print("3. Exit")
        
        	choice = int(input("Enter your choice: "))
        
        	if choice == 1:
            		input_graph()
        	elif choice == 2:
            		prims_mst(graph)
        	elif choice == 3:
            		print("Exiting...")
            		break
        	else:
            		print("Invalid choice! Please try again.")

main()
# END OF CODE
