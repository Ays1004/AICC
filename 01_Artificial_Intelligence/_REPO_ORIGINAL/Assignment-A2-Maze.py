# Assignment-A2 (A* Algorithm for Game Search)

"""
THIS CODE HAS BEEN TESTED AND IS FULLY OPERATIONAL.

Problem Statement: Implement A star Algorithm for any game search problem.

Code from ArtificialIntelligence (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/ArtificialIntelligence
"""

# This code implements A* algorithm for maze game solving since the problem
# statement in our syllabus (but not our handout) demands implementing A* 
# algorithm for any game search problem.

# A* implementation for 8 puzzle problem can be found in the "Codes" folder
# and direct implementation can be found in the "Alternatives" folder.

# BEGINNING OF CODE
print("Maze game solving")

# Directions: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x
        self.y = y
        self.g = g # cost to reach the node from the start
        self.h = h # estimated cost from node to goal (heuristic)
        self.f = g + h
        self.parent = parent

def heuristic(x1, y1, x2, y2):  # Manhattan distance
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start[0], start[1], 0, heuristic(start[0], start[1], goal[0], goal[1]))  #Node(x, y, g, h)
    open_list.append(start_node)

    while open_list:
        # Find node with lowest f in open_list
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)

        if (current_node.x, current_node.y) == goal:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_set.add((current_node.x, current_node.y))

        for direction in DIRECTIONS:
            nx, ny = current_node.x + direction[0], current_node.y + direction[1]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in closed_set:
                g = current_node.g + 1
                h = heuristic(nx, ny, goal[0], goal[1])
                neighbor = Node(nx, ny, g, h, current_node)
                open_list.append(neighbor)

    return None

def get_user_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    grid = []
    print("Enter the grid row by row (1 for walkable, 0 for blocked):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        grid.append(row)

    start = tuple(map(int, input("Enter start point (row col): ").split()))
    goal = tuple(map(int, input("Enter goal point (row col): ").split()))
    return grid, start, goal

def main():
    # Get the user input for the grid, start, and goal positions
    grid, start, goal = get_user_input()

    # Call the A* algorithm to find the path
    path = a_star(grid, start, goal)

    # Print the result based on whether a path is found or not
    if path:
        print("Path found:", path)
    else:
        print("No path found.")

main()
# END OF CODE

# NOTE: IN THE MATRIX FORMED (ROWS+COLUMN WALA), THE TOP LEFT CELL HAS VALUE (0,0).
# For eg.: If you're making a 3x3 matrix, top left corner will have value (0,0)
# and, bottom right corner will have value (2,2).

"""
SAMPLE OUTPUT:

Maze game solving
Enter number of rows: 3
Enter number of columns: 3
Enter the grid row by row (1 for walkable, 0 for blocked):
Row 1: 1 0 1
Row 2: 1 1 1
Row 3: 0 0 1
Enter start point (row col): 0 0
Enter goal point (row col): 2 2
Path found: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
"""
