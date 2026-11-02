# Assignment-3 (Alternative)

"""
THIS CODE HAS BEEN TESTED AND IS FULLY OPERATIONAL.

Problem Statement: Implement Greedy search algorithm for any of the following application:
  I. Selection Sort
  V. Prim's Minimal Spanning Tree Algorithm

Code from ArtificialIntelligence (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/ArtificialIntelligence
"""

# BEGINNING OF CODE
numbers = []
graph = []

# BEGINNING OF SELECTION SORT
# Input numbers
def input_number():
    total = int(input("Enter total numbers: "))
    for i in range(total):
        val = float(input("Enter number: "))
        numbers.append(val)
    print("Numbers you entered:", numbers)

# Perform selection sort
def selection_sort():
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print("Sorted numbers:", numbers)
# END OF SELECTION SORT

# BEGINNING OF PRIM'S MST
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
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 999 and i != j:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        no_of_edges += 1

# Function to input graph as adjacency matrix
def input_graph():
    V = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix row by row:")
    for i in range(V):
        row = list(map(int, input(f"Row {i}: ").split()))
        graph.append(row)
# END OF PRIM'S MST


# Main menu-driven function
def main():
    while True:
        print("\nMenu:")
        print("1. Input numbers and perform selection sort")
        print("2. Perform selection sort")
        print("3. Input graph")
        print("4. Run Prim's MST algorithm")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            input_number()
        elif choice == 2:
            selection_sort()
        elif choice == 3:
            input_graph()
        elif choice == 4:
            prims_mst(graph)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

main()
# END OF CODE
