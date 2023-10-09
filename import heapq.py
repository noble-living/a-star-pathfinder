import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic cost (estimated cost from current node to goal)
        self.f = 0  # Total cost (g + h)

def astar(grid, start, end):
    open_list = []
    closed_list = []

    start_node = Node(start)
    goal_node = Node(end)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)

        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return the reversed path

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Four possible movement directions

        for neighbor in neighbors:
            new_position = (
                current_node.position[0] + neighbor[0],
                current_node.position[1] + neighbor[1],
            )

            if (
                new_position[0] < 0
                or new_position[0] >= len(grid)
                or new_position[1] < 0
                or new_position[1] >= len(grid[0])
            ):
                continue  # Skip if the neighbor is out of bounds

            if grid[new_position[0]][new_position[1]] == 1:
                continue  # Skip if the neighbor is an obstacle

            neighbor_node = Node(new_position, current_node)
            if neighbor_node in closed_list:
                continue  # Skip if the neighbor is already evaluated

            neighbor_node.g = current_node.g + 1  # Assuming a cost of 1 between nodes
            neighbor_node.h = (
                abs(neighbor_node.position[0] - goal_node.position[0])
                + abs(neighbor_node.position[1] - goal_node.position[1])
            )
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if neighbor_node not in open_list:
                open_list.append(neighbor_node)

    return None  # If no path is found

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found.")
